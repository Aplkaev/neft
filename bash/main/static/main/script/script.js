Dropzone.autoDiscover = false;
$(function() {



    new Dropzone("#form_dropzone", {
        maxFilesize: 500, // MB
        init: function() {
            this.on("success", function(file, response) {
                console.log(response);
                if (response.result == 'error') {
                    $(file.previewElement).addClass("dz-error").find('.dz-error-message').text(response.result);
                } else {
                    $.each(response.result.data, (key, value) => {
                        $('form').append(`<input type="hidden" name="files[]" value="${value}">`);
                    })

                }

            });
        }
    });

});

function show_log(log) {
    $('.log').html(log);
}

function load_log() {
    $.ajax({
        url: '/log',
        success: (response) => {
            // console.log(response);
            show_log(response);
        }
    });
}