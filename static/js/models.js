$(document).ready(function(){
	/* bookings */
    Booking = Model.extend();
    Bookings = Collection.extend({
        model: Booking,
        comparator: '-start'
    }); 
    
    /* projects */
    Project = Model.extend({
    	// methods
    	getBookingById: function(id) {
    		var index = this.get('bookings').map(function(x) {return x.id; }).indexOf(parseInt(id));
    		if(index >= 0) {
    			return new Booking(this.get('bookings')[index]);
    		} else {
    			return null;
    		}
    	}    	
    });
    Projects = Collection.extend({
    	model: Project,
    }); 
});