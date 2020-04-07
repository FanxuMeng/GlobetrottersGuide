$(document).ready(function(){
	$('#search-input').keyup(function(){//change search=input to the name of the element
		var query;
		query = $(this).val();
		
		$.get('/GlobetrottersGuide/suggest',{'suggestion':query},function(data){
			$('listarea').html(data);
		})
	})
})
//not final, subject to changes: check views.py and urls.py for some reference