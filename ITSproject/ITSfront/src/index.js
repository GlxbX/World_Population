
$(document).ready(function () {

    //Модальное окно

    const modalCall = $('[data-modal]')


    modalCall.on('click', function (event) {
        event.preventDefault();

        let $this = $(this)
        let modalId = $this.data('modal')

        $(modalId).addClass('show')
        $('body').addClass('no-scroll')

        console.log(modalId)
    })

    $('.popup').on('click', function (event) {

        $(this).removeClass('show')
        $('body').removeClass('no-scroll')
    })


    $('.popup__wrapper').on('click', function (event) {
        event.stopPropagation()
    })

    $('.fa-times-circle').on('click', function (event) {
        $('.popup').removeClass('show')
        $('body').removeClass('no-scroll')
    })

});