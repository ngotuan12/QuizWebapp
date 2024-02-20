$(document).ready(function(){
	$('#stacked-menu .menu-link').each(function(){
		var pathname = window.location.pathname;
		if( $(this).hasClass('home'))
		{
			if(pathname == $(this).attr('href'))
			{
				var menuChildren = $(this);
				menuChildren.parent().addClass("has-active");
				menuChildren.closest(".has-child").addClass("has-open");
			}
		}
		else if(pathname.indexOf($(this).attr('href'))>=0)
		{
			var menuChildren = $(this);
			menuChildren.parent().addClass("has-active");
			menuChildren.closest(".has-child").addClass("has-open");
		}
	});
	
	$('#stacked-menu .has-child').each(function(){
		if( $(this).find('ul.menu .menu-item').length == 0 )
			$(this).hide();
	});
});