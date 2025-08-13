 // Current date and time
        function updateDateTime() {
            const now = new Date();
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            document.getElementById('current-date').textContent = now.toLocaleDateString('en-US', options);
            document.getElementById('current-time').textContent = now.toLocaleTimeString('en-US');
        }
        
        setInterval(updateDateTime, 1000);
        updateDateTime();

    const ticker = document.querySelector('.ticker-item');
        let position = 0;
        
        function animateTicker() {
            position -= 1;
            ticker.style.transform = `translateX(${position}px)`;
            
            if (position < -ticker.offsetWidth) {
                position = document.querySelector('.news-ticker').offsetWidth;
            }
            
            requestAnimationFrame(animateTicker);
        }
        
        animateTicker();


