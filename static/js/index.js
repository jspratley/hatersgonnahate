$(document).ready(function() {
    $('#search').on('click', function () {
        if ($('input[name="search"]').val().length === 0) {
            alert('Please enter a username');
            return;
        } else {
            $.getJSON($SCRIPT_ROOT + '/search', {
                searchText: $('input[name="search"]').val()
            }, function(data) {
                for (var res in data.result) {
                    $('#results').append('<li>' + data.result[res]['name'] + ' ' + data.result[res]['screen_name'] + ' ' +
                    data.result[res]['user_id'] + '</li>');
                    if (data.result[res]['on_block_list'] === "Yes") {
                        $('#results').append('<p>Blocked</p>');
                    } else {
                        $('#results').append('<button class="btn btn-primary block" id="' + data.result[res]['screen_name'] + '">Block</button');
                    }
                }
            });
            return false;
        }
    });

    $(document).on('click', '.block', function () {
        var button = $(this);
        $.getJSON($SCRIPT_ROOT + '/block', {
            screenName: $(this).attr('id')
        }, function(data) {
            alert(data.result);
            button.replaceWith('<p>Blocked</p>');
        });
    });
});