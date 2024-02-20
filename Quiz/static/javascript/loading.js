/**
 * @author: TuanNA
 * @since: 11/09/2014
 * @version: 1.0 Copyright 2014, Ngo Anh Tuan
 */
(function($)
{
	
	
	$.fn.loading = {
		show: function()
		{
//			$('body').css("overflow","hidden");
			$.loading.loadMask();
			//addloading
			loading = $('<div id="loading" style="top:50%;left:50%;position:fixed;z-index:1000"><i style="font-size:28px"class="fa fa-spinner fa-spin"></i></div>');
			loading.appendTo('body');

		},
		hide: function()
		{
//			$('body').css("overflow","");
			$('body #loading').remove();
			$('#background-mask').remove();
			/*return new Promise((resolve, reject) => {
				
				$('#loading').fadeOut(function()
				{
					
					resolve();
				});
			});*/
		},
	};
	var mask, size, loading;
	
	$.loading = {
		loadMask: function()
		{
			mask = $('<div id="background-mask" />').appendTo($('body'));
			mask.css({
				position : 'fixed',
				top : 0,
				left : 0,
				width : '100%',
				height : '100%',
				display : 'none',
				opacity : 0,
				zIndex : 9999,
				backgroundColor : '#000'
			});

			mask.css({
				display : 'block'
			}).fadeTo('400', 0);

		},
	};
})(jQuery);
