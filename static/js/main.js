// display message
$(function() {
	var message_base = {
			alert: function(severity, message) {
				var html = templates.alert({severity, message});
				$("#messages").append(html);
			}
	}
	message = {
		success: 	function(message) {message_base.alert('success', message)},
		info: 		function(message) {message_base.alert('info', message)},
		warning: 	function(message) {message_base.alert('warning', message)},
		danger: 	function(message) {message_base.alert('danger', message)}
	}	
});