var project;

$(function() {
	/* data store */
	project = new Project(project_as_json);
		
	// utility
	function deleteBooking(target, id) {
		$(target).slideUp();
		var booking = project.getBookingById(id);
		var deleteTemplate = _.template(
				'Booking for <%= name %> at <%= date %> - <%= time %> ' +
				'will be deleted when this project is saved. ' +
				'(<a href="#" class="undo-delete" data-target="<%= target %>">undo</a>)'
		);
		var msg = deleteTemplate({
			name: booking.get('resource_name'),
			date: booking.get('date'),
			time: booking.get('start_time'),
			target: target,
			id: id,
		})
		message.info(msg);
		// setup the click handler for undo
		$('a.undo-delete').click(function() {
			event.preventDefault();
			var target = $(this).attr('data-target');
			undeleteBooking(target);
			$(this).closest('.alert').fadeOut();
		});
	}
	function undeleteBooking(target) {
		$(target).slideDown();
	}
	
	/* setup booking action handlers */
	$('.delete-booking').click(function(event) {
		event.preventDefault();
		var target = $(this).attr('data-target');
		var pk = $(this).attr('data-pk');
		deleteBooking(target, pk);
	});
});

// wait until everything else is done then init the datetime pickers and select2s since they take a while
window.onload = function() {
	$('.datetimepicker').datetimepicker({
		format: "MM dd yyyy - HH:ii P",
        showMeridian: true,
        autoclose: true,
        todayBtn: true,
        minuteStep: 5,
    });
	$('.select2').select2({});
	$('.move-booking').editable({
		source: urls.api.projects + '?format=select',
		success: function(response, value) {
			var pk = $(this).next().find('select').val();
			var name = $(this).next().find('select option:selected').text();
			var movedTemplate = _.template(
					'Booking for <%= name %> at <%= date %> - <%= time %> ' +
					'will be moved to <%= project %> when this project is saved. '
			);
			var id = $(this).attr('data-pk');
			var booking = project.getBookingById(id);
			message.info(movedTemplate({
				name: booking.get('resource_name'),
				date: booking.get('date'),
				time: booking.get('start_time'),
				project: name,
			}));
			$(this).closest('.panel-group').find('.project_input').val(pk);
			return true;
		},
	});
};

