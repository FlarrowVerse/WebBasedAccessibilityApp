function openWebsite() {
	var url = document.getElementById('main-form').elements[0].value;
	console.log('Opening the URL: ' + url);

	$.get(url, function(data) {
		window.alert(data);
	});

	window.open('https://translate.google.com/translate?sl=auto&tl=bn&u=' + url, target='_blank');
	
}