document.addEventListener('DOMContentLoaded', function () {
    const calendar = document.getElementById('calendar');
    const info = document.getElementById('info');
    const servicesSelect = document.getElementById('services');
    const timesSelect = document.getElementById('times');
    const doctorsSelect = document.getElementById('doctors');
    const bookingForm = document.getElementById('booking-form');

    const clinicData = {
        "2024-06-06": {
            services: ["Consulta Geral", "Pediatria", "Dermatologia"],
            times: ["08:00", "10:00", "14:00", "16:00"],
            doctors: ["Dr. Silva", "Dra. Maria", "Dr. João"]
        },
        // Adicione mais dias e dados conforme necessário
    };

    function updateDetails(date) {
        const data = clinicData[date];

        if (data) {
            info.textContent = `Serviços, horários e médicos disponíveis para o dia ${date}:`;
            servicesSelect.innerHTML = data.services.map(service => `<option value="${service}">${service}</option>`).join('');
            timesSelect.innerHTML = data.times.map(time => `<option value="${time}">${time}</option>`).join('');
            doctorsSelect.innerHTML = data.doctors.map(doctor => `<option value="${doctor}">${doctor}</option>`).join('');
        } else {
            info.textContent = `Nenhum serviço disponível para o dia ${date}.`;
            servicesSelect.innerHTML = '';
            timesSelect.innerHTML = '';
            doctorsSelect.innerHTML = '';
        }
    }

    function createCalendar() {
        const now = new Date();
        const month = now.getMonth();
        const year = now.getFullYear();

        calendar.innerHTML = '';
        const monthDays = new Date(year, month + 1, 0).getDate();

        for (let i = 1; i <= monthDays; i++) {
            const day = new Date(year, month, i);
            const dateStr = day.toISOString().split('T')[0];

            const dayDiv = document.createElement('div');
            dayDiv.classList.add('day');
            dayDiv.textContent = i;

            dayDiv.addEventListener('click', function () {
                updateDetails(dateStr);
            });

            calendar.appendChild(dayDiv);
        }
    }

    createCalendar();

    bookingForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const selectedService = servicesSelect.value;
        const selectedTime = timesSelect.value;
        const selectedDoctor = doctorsSelect.value;
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        alert(`Consulta agendada com sucesso!\n\nServiço: ${selectedService}\nHorário: ${selectedTime}\nMédico: ${selectedDoctor}\nNome: ${name}\nEmail: ${email}`);
    });
});
