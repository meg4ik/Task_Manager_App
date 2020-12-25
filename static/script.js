'use strict';
        (function (window, document, $) {
        function sendRequest() {
            $.ajax({
                type: "POST", 
                url: 'http://127.0.0.1:5000{{clink}}',
                data: $("#contentform").serialize(),
            });
        }

        $(document).ready(function() {
            $('#button').click(function() {
                sendRequest();
            });
        });
    })(window, document, jQuery);