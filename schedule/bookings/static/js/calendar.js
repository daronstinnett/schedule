var Calendar;
var calendar;
var $calendar;
var Booking;
var Bookings;
var bookings;
var ResourceSelectView;
var resourceSelectView;
var BookingsListView;
var bookingsListView

var currentResource = {
	get: function getCurrentResource() {
		// query param is the priority
		if(urlParams.resource) {
			// save to cookie
			$.cookie('schedule_resource', urlParams.resource);
		}
		return $.cookie('schedule_resource');
	},
	set: function saveCurrentResource(id) {
		$.cookie('schedule_resource', id);
	}
}


$(document).ready(function(){
	/* data sets */
    CalendarBookings = Bookings.extend({
        url: urls.api.bookings,
    }); 
    bookings = new CalendarBookings();
 
    /* views */
    ResourceSelectView = View.extend({
    	el: '#resourceSelect',
    	render: function() {
    		$(this.el).val(currentResource.get());
    		$(this.el).select2({});
    	},
    	getResource: function() {
    		return $(this.el).val();
    	}
    });
    resourceSelectView = new ResourceSelectView();
    resourceSelectView.render();
    
    BookingsListView = View.extend({
    	el: '#bookingsList',
    	initialize: function() {
    		this.template = _.template($("#bookingListTemplate").html());
    		bookings.on('reset change', this.render, this);		
    	},
    	render: function() {
    		var now = moment().toISOString();
    		var pastBookings = new Collection(bookings.query({end: {$lt: now}})); 
    		var upcomingBookings = new Collection(bookings.query({end: {$gt: now}})); 
			$('#bookingsList').html(this.template({
				pastBookings: pastBookings.toJSON(),
				upcomingBookings: upcomingBookings.toJSON()
			}));
    	}
    });
    bookingsListView = new BookingsListView();
    
    Calendar = Backbone.View.extend({
        initialize: function(){
        	var bookings = this.collection;
        	bookings.on('reset', this.addAll, this);
        	bookings.on('add', this.addOne, this);
        	bookings.on('change', this.change, this);            
        	bookings.on('destroy', this.destroy, this);
        	
        	$("#cal-controls button").click(function() {
        		var args = $(this).attr('data-function').split(' ');
        		$calendar.fullCalendar.apply($calendar, args);
        	});
            
            this.bookingView = new EventView();  
            var func = _.bind(this.filterBySelectedResource, this);
            $(resourceSelectView.el).on('change', func);
        },
        render: function() {
        	var date = moment();
        	if(!isNaN($.cookie('schedule_fc_date'))) {
        		date = moment(parseInt($.cookie('schedule_fc_date')));
        	}
            $(this.el).fullCalendar({
                header: {
                    left: '',
                    center: '',
                    right: ''
                },
                defaultView: $.cookie('schedule_fc_view') || 'agendaWeek',
                defaultDate: date,
                selectable: true,
                selectHelper: true,
                editable: true,
                firstDay: 1,
                ignoreTimezone: false,                
                select: _.bind(this.select, this),
                eventClick: _.bind(this.eventClick, this),
                eventDrop: _.bind(this.eventDropOrResize, this),        
                eventResize: _.bind(this.eventDropOrResize, this),
                viewRender: _.bind(this.viewRender, this)
            });
            // remove calendar header
            $('.fc-toolbar').remove();
        },
        addAll: function() {
            $(this.el).fullCalendar('addEventSource', this.collection.toJSON());
        },
        addOne: function(event) {
        	$(this.el).fullCalendar('renderEvent', event.toJSON());
        },        
        select: function(startDate, endDate) {
            this.eventView.collection = this.collection;
            this.eventView.model = new Event({start: startDate, end: endDate});
            this.eventView.render();            
        },
        eventClick: function(fcEvent) {
        	var instance = this.collection.get(fcEvent.id);
        	var params = $.param({booking:instance.get("id"), success_url:window.location.href});
        	var url = urls.templates.projects({id:instance.get('project')})+"?"+params;
        	window.location.href = url;
            //this.eventView.model = this.collection.get(fcEvent.id);
            //this.eventView.render();
        },
        change: function(event) {
            // Look up the underlying event in the calendar and update its details from the model
            var fcEvent = $(this.el).fullCalendar('clientEvents', event.get('id'))[0];
            fcEvent.title = event.get('title');
            fcEvent.color = event.get('color');
            $(this.el).fullCalendar('updateEvent', fcEvent);           
        },
        filterBySelectedResource: function() {
        	var id = $(resourceSelectView.el).val();
        	var query = {};
        	if(id) {
        		query = $.extend(query, {resource__id:id});
        	}
        	$(this.el).fullCalendar('removeEvents');
        	this.collection.fetch({reset: true, data:query});
        	currentResource.set(id);
        },
        eventDropOrResize: function(fcEvent) {
            // Lookup the model that has the ID of the event and update its attributes
            this.collection.get(fcEvent.id).save({start: fcEvent.start, end: fcEvent.end});            
        },
        destroy: function(event) {
        	$(this.el).fullCalendar('removeEvents', event.id);         
        },
        saveSettings: function(view) {
        	$.cookie('schedule_fc_view', view.name);
        	$.cookie('schedule_fc_date', $(this.el).fullCalendar( 'getDate' ).valueOf());
        },
        viewRender: function(view, element) {
        	this.saveSettings(view);
        	var formattedDate;
        	if(view.name == "month") {
        		formattedDate = $(this.el).fullCalendar('getDate').format("MMMM YYYY");
        	} else {
        		formattedDate = $(this.el).fullCalendar('getDate').format("MMM DD YYYY");
        	}
        	$("#cal-current-date").html(formattedDate);
        }
    });

    var EventView = Backbone.View.extend({
        el: $('#eventDialog'),
        initialize: function() {
        },
        render: function() {
            var buttons = {'Ok': this.save};
            if (!this.model.isNew()) {
                _.extend(buttons, {'Delete': this.destroy});
            }
            _.extend(buttons, {'Cancel': this.close});            
            
            this.el.dialog({
                modal: true,
                title: (this.model.isNew() ? 'New' : 'Edit') + ' Event',
                buttons: buttons,
                open: this.open
            });

            return this;
        },        
        open: function() {
            this.$('#title').val(this.model.get('title'));
            this.$('#color').val(this.model.get('color'));            
        },        
        save: function() {
            this.model.set({'title': this.$('#title').val(), 'color': this.$('#color').val()});
            
            if (this.model.isNew()) {
                this.collection.create(this.model, {success: this.close});
            } else {
                this.model.save({}, {success: this.close});
            }
        },
        close: function() {
            this.el.dialog('close');
        },
        destroy: function() {
            this.model.destroy({success: this.close});
        }        
    });
    calendar = new Calendar({el: $("#calendar"), collection: bookings});
    calendar.render();
    $calendar = $(calendar.el);
    calendar.filterBySelectedResource();
});