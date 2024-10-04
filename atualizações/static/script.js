document.addEventListener('DOMContentLoaded', function () {
    const formAgendamento = document.querySelector('form[action="/agendar"]');

    if (formAgendamento) {
        formAgendamento.addEventListener('submit', function (event) {
            event.preventDefault(); // Evita o comportamento padrão do envio do formulário

            const idMedico = document.querySelector('input[name="id_medico"]').value;
            const idServico = document.querySelector('input[name="id_servico"]').value;
            const data = document.querySelector('input[name="data"]').value;
            const horaInicio = document.querySelector('input[name="hora_inicio"]').value;

            // Verifica se todos os campos obrigatórios estão preenchidos
            if (idMedico && idServico && data && horaInicio) {
                // Cria o objeto de dados que será enviado
                const dadosAgendamento = {
                    id_medico: idMedico,
                    id_servico: idServico,
                    data: data,
                    hora_inicio: horaInicio
                };

                // Envia os dados via POST para o backend
                fetch('/agendar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dadosAgendamento)
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Erro ao agendar');
                    }
                })
                .then(data => {
                    if (data.sucesso) {
                        alert('Agendamento realizado com sucesso!');
                        window.location.href = '/confirmacao'; // Redireciona para a página de confirmação
                    } else {
                        alert('Erro ao realizar o agendamento. Tente novamente.');
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Ocorreu um erro ao tentar realizar o agendamento.');
                });
            } else {
                alert('Por favor, preencha todos os campos obrigatórios.');
            }
        });
    }
});
