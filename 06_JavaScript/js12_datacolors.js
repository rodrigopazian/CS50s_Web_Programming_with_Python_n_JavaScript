document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function () {
            document.querySelector('#colors').style.color = button.dataset.color;
        }
    })
});
