'use strict';
        (function (window, document, $) {
        function sendRequest() {
            var request = $.ajax({
                url: 'http://127.0.0.1:5000{{clink}}',
                data : $("#contentform").serialize(),
                dataType: 'json',
                type: 'post'
            });


            request.fail(function() {
              alert("fail!")
            });
        }

        $(document).ready(function() {
            $('#button').click(function() {
                sendRequest();
            });
        });
    })(window, document, jQuery);