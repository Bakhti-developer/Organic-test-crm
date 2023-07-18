$(function() {


      // chart1
      var ctx = document.getElementById('chart1').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'doughnut',
          data: {
              labels: ['Organic', 'Paid', 'Email', 'Direct', 'Social', 'Affiliates'],
              datasets: [{
                  data: [12, 19, 3, 5, 2, 3],
                  backgroundColor: [
                      '#923eb9',
                      '#f73757',
                      '#18bb6b',
                      '#32bfff',
                      '#ffab4d',
                      '#0a58ca'
                  ],
                  borderWidth: 1
              }]
          },
          options: {
             maintainAspectRatio: false,
             cutout: 125,
             plugins: {
                legend: {
                    display: false,
                }
            }
             
          }
      });
    


    // chart2
    var ctx = document.getElementById('chart2').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Orders',
                data: [12, 19, 13, 15, 20, 10],
                backgroundColor: [
                    '#923eb9'
                ],
                borderColor: [
                    '#923eb9'
                ],
                borderWidth: 0
            },
            {
                label: 'Visits',
                data: [7, 15, 9, 12, 17, 16],
                backgroundColor: [
                    'rgb(146 62 185 / 32%)'
                ],
                borderColor: [
                    'rgb(146 62 185 / 32%)'
                ],
                borderWidth: 0
            }]
        },
        options: {
            maintainAspectRatio: false,
            barPercentage: 0.3,
            //categoryPercentage: 0.5,
            plugins: {
                legend: {
                    display: false,
                }
            },
            scales: {
                x: {
                  stacked: true,
                  beginAtZero: true
                },
                y: {
                  stacked: true,
                  beginAtZero: true
                }
              }
        }
    });



    // chart3
    var ctx = document.getElementById('chart3').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jun'],
            datasets: [{
                label: 'Electronics',
                data: [12, 10, 13, 25, 14, 10, 14],
                backgroundColor: [
                    '#923eb9'
                ],
                /* fill: {
                    target: 'origin',
                    above: 'rgb(146 62 185 / 21%)',   // Area will be red above the origin
                    below: 'rgb(146 62 185 / 21%)'    // And blue below the origin
                  }, */
                tension: 0.4,
                borderColor: [
                    '#923eb9'
                ],
                borderWidth: 3
            },
            {
                label: 'Furniture',
                data: [8, 15, 9, 18, 10, 16, 8],
                backgroundColor: [
                    '#18bb6b'
                ],
                fill: {
                    target: 'origin',
                    above: 'rgb(24 187 107 / 21%)',   // Area will be red above the origin
                    below: 'rgb(24 187 107 / 21%)'    // And blue below the origin
                  },
                tension: 0.4,
                borderColor: [
                    '#18bb6b'
                ],
                borderWidth: 3
            }]
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false,
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });




      // chart4
      var ctx = document.getElementById('chart4').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'pie',
          data: {
              labels: ['Clothing', 'Electronics', 'Furniture'],
              datasets: [{
                  data: [55, 20, 10],
                  backgroundColor: [
                      '#0a58ca',
                      '#18bb6b',
                      '#ffab4d'
                  ],
                  borderWidth: 1
              }]
          },
          options: {
             maintainAspectRatio: false,
             cutout: 0,
             plugins: {
                legend: {
                    display: false,
                }
            }
             
          }
      });




  
    
});