// JavaScript to hide the preloader once the page is fully loaded
$(window).on('load', function () {
    $('#preloader').fadeOut('slow', function () {
        $(this).remove();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const profileButton = document.querySelector('.relative button');
    const dropdownMenu = document.querySelector('.relative .absolute');

    if (profileButton) {
        profileButton.addEventListener('click', () => {
            dropdownMenu.classList.toggle('hidden');
        });

        document.addEventListener('click', (event) => {
            if (!profileButton.contains(event.target)) {
                dropdownMenu.classList.add('hidden');
            }
        });
    }
});
