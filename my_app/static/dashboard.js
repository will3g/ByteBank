/* globals Chart:false, feather:false */

(function () {
  'use strict'

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Domingo',
        'Segunda',
        'Terça',
        'Quarta',
        'Quinta',
        'Sexta',
        'Sábado'
      ],
      datasets: [{
        data: [
          16.80,
          14.15,
          10.50,
          9.13,
          8.15,
          7.75,
          5.50
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#18b52e',
        borderWidth: 4,
        pointBackgroundColor: '#18b52e'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
}())