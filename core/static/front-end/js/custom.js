jQuery(document).ready(function($) {
    "use strict"


	// ------- Filter Gallery Start ------- //
	if ($('.filter-gallery').length) {
		if ($('.filter-gallery .isotope').length) {
			var $container = $('.filter-gallery .isotope');
			$container.isotope({
				itemSelector: '.item',
				transitionDuration: '0.6s',
				masonry: {
					columnWidth: $container.width() / 12
				},
				layoutMode: 'masonry'
			});
			$(window).on("resize", function() {
				$container.isotope({
					masonry: {
						columnWidth: $container.width() / 12
					}
				});
			});
		}
		if ($('.filter-gallery #filters').length) {
			$('.filter-gallery #filters').on('click', 'button', function() {
				var filterValue = $(this).attr('data-filter');
				$container.isotope({
					filter: filterValue
				});
			});
			// change is-checked class on buttons
			$('.filter-gallery .button-group').each(function(i, buttonGroup) {
				var $buttonGroup = $(buttonGroup);
				$buttonGroup.on('click', 'button', function() {
					$buttonGroup.find('.is-checked').removeClass('is-checked');
					$(this).addClass('is-checked');
				});
			});
	
		}
	}

}
