$(document).ready(function() {
    $('#scrape_tvshows_btn').click(function() {
        $.ajax( {
            url:'/scrape-tvshows/',
            type: 'GET',
            success: function (data) {
                alert('Scraped successfully');
            },
            error: function () {
                alert('An error occurred while scraping the data ');
            }
        });
    });
});