$(function() {

   
// chart 1
var options = {
    series: [{
        name: "Total Earnings",
       // data: [0, 160, 671, 414, 555, 257, 901, 613, 727, 414, 555, 0]
        data: [0, 160, 671, 414, 555, 414, 555, 257, 300, 0]
    }],
    chart: {
        type: "area",
        //width: 130,
        height: 70,
        toolbar: {
            show: !1
        },
        zoom: {
            enabled: !1
        },
        dropShadow: {
            enabled: 0,
            top: 3,
            left: 14,
            blur: 4,
            opacity: .12,
            color: "#923eb9"
        },
        sparkline: {
            enabled: !0
        }
    },
    markers: {
        size: 0,
        colors: ["#923eb9"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7
        }
    },
    plotOptions: {
        bar: {
            horizontal: !1,
            columnWidth: "30%",
            endingShape: "rounded"
        }
    },
    dataLabels: {
        enabled: !1
    },
    stroke: {
        show: !0,
        width: 0,
        curve: "smooth"
    },
    xaxis: {
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    },
    fill: {
		type: 'gradient',
		gradient: {
		  shade: 'light',
		  type: 'vertical',
		  shadeIntensity: 0.5,
		  gradientToColors: ['#7928ca'],
		  inverseColors: false,
		  opacityFrom: 1,
		  opacityTo: 1,
		  //stops: [0, 100]
		}
	  },
    colors: ["#ff0080"],
    tooltip: {
        theme: "dark",
        fixed: {
            enabled: !1
        },
        x: {
            show: !1
        },
        y: {
            title: {
                formatter: function(e) {
                    return ""
                }
            }
        },
        marker: {
            show: !1
        }
    }
  };

  var chart = new ApexCharts(document.querySelector("#chart1"), options);
  chart.render();




// chart 2
var options = {
    series: [{
        name: "Total Expense",
        data: [0, 160, 671, 414, 555, 414, 555, 257, 300, 0]
    }],
    chart: {
        type: "area",
        //width: 130,
        height: 70,
        toolbar: {
            show: !1
        },
        zoom: {
            enabled: !1
        },
        dropShadow: {
            enabled: 0,
            top: 3,
            left: 14,
            blur: 4,
            opacity: .12,
            color: "#ee0979"
        },
        sparkline: {
            enabled: !0
        }
    },
    markers: {
        size: 0,
        colors: ["#ee0979"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7
        }
    },
    plotOptions: {
        bar: {
            horizontal: !1,
            columnWidth: "30%",
            endingShape: "rounded"
        }
    },
    dataLabels: {
        enabled: !1
    },
    stroke: {
        show: !0,
        width: 0,
        curve: "smooth"
    },
    xaxis: {
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    },
    fill: {
		type: 'gradient',
		gradient: {
		  shade: 'light',
		  type: 'vertical',
		  shadeIntensity: 0.5,
		  gradientToColors: ['#ee0979'],
		  inverseColors: false,
		  opacityFrom: 1,
		  opacityTo: 1,
		  //stops: [0, 100]
		}
	  },
    colors: ["#ff6a00"],
    tooltip: {
        theme: "dark",
        fixed: {
            enabled: !1
        },
        x: {
            show: !1
        },
        y: {
            title: {
                formatter: function(e) {
                    return ""
                }
            }
        },
        marker: {
            show: !1
        }
    }
  };

  var chart = new ApexCharts(document.querySelector("#chart2"), options);
  chart.render();




// chart 3
var options = {
    series: [{
        name: "Total Orders",
        data: [0, 160, 671, 414, 555, 414, 555, 257, 300, 0]
    }],
    chart: {
        type: "area",
        //width: 130,
        height: 70,
        toolbar: {
            show: !1
        },
        zoom: {
            enabled: !1
        },
        dropShadow: {
            enabled: 0,
            top: 3,
            left: 14,
            blur: 4,
            opacity: .12,
            color: "#009efd"
        },
        sparkline: {
            enabled: !0
        }
    },
    markers: {
        size: 0,
        colors: ["#009efd"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7
        }
    },
    plotOptions: {
        bar: {
            horizontal: !1,
            columnWidth: "30%",
            endingShape: "rounded"
        }
    },
    dataLabels: {
        enabled: !1
    },
    stroke: {
        show: !0,
        width: 0,
        curve: "smooth"
    },
    xaxis: {
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    },
    fill: {
		type: 'gradient',
		gradient: {
		  shade: 'light',
		  type: 'vertical',
		  shadeIntensity: 0.5,
		  gradientToColors: ['#009efd'],
		  inverseColors: false,
		  opacityFrom: 1,
		  opacityTo: 1,
		  //stops: [0, 100]
		}
	  },
    colors: ["#2af598"],
    tooltip: {
        theme: "dark",
        fixed: {
            enabled: !1
        },
        x: {
            show: !1
        },
        y: {
            title: {
                formatter: function(e) {
                    return ""
                }
            }
        },
        marker: {
            show: !1
        }
    }
  };

  var chart = new ApexCharts(document.querySelector("#chart3"), options);
  chart.render();




  // chart4
    var ctx = document.getElementById('chart4').getContext('2d');

    var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
        gradientStroke1.addColorStop(0, '#009efd');
        gradientStroke1.addColorStop(1, '#2af598');

    var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 300);
        gradientStroke2.addColorStop(0, '#7928ca');  
        gradientStroke2.addColorStop(1, '#ff0080'); 

    var gradientStroke3 = ctx.createLinearGradient(0, 0, 0, 300);
        gradientStroke3.addColorStop(0, '#ff8359');
        gradientStroke3.addColorStop(1, '#ffdf40');


    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            datasets: [{
                label: 'Avg. Session',
                data: [15, 22, 13, 15, 20, 10, 15],
                backgroundColor: [
                    gradientStroke1
                ],
                borderColor: [
                    gradientStroke1
                ],
                borderWidth: 0,
                borderRadius: 20
            },
            {
                label: 'Conversion. Rate',
                data: [20, 35, 30, 35, 28, 22, 25],
                backgroundColor: [
                    gradientStroke2
                ],
                borderColor: [
                    gradientStroke2
                ],
                borderWidth: 0,
                borderRadius: 20
            },{
                label: 'Avg. Session Duration',
                data: [10, 15, 9, 12, 17, 16, 10],
                backgroundColor: [
                    gradientStroke3
                ],
                borderColor: [
                    gradientStroke3
                ],
                borderWidth: 0,
                borderRadius: 20
            }]
        },
        options: {
            maintainAspectRatio: false,
            barPercentage: 0.9,
            categoryPercentage: 0.4,
            plugins: {
                legend: {
                    maxWidth: 20,
                    boxHeight: 20,
                    position:'bottom',
                    display: true,
                }
            },
            scales: {
                x: {
                  stacked: false,
                  beginAtZero: true
                },
                y: {
                  stacked: false,
                  beginAtZero: true
                }
              }
        }
    });
 


// chart5
var ctx = document.getElementById('chart5').getContext('2d');

var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke1.addColorStop(0, '#005bea');
    gradientStroke1.addColorStop(1, '#00c6fb');

var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke2.addColorStop(0, '#ff6a00');  
    gradientStroke2.addColorStop(1, '#ee0979'); 

var gradientStroke3 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke3.addColorStop(0, '#17ad37');  
    gradientStroke3.addColorStop(1, '#98ec2d'); 

var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Desktop', 'Mobile', 'Tablet'],
        datasets: [{
            data: [155, 120, 110],
            backgroundColor: [
                gradientStroke1,
                gradientStroke2,
                gradientStroke3,
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        cutout: 110,
        plugins: {
        legend: {
            display: false,
        }
    }
        
    }
});



  // chart6
  var ctx = document.getElementById('chart6').getContext('2d');

  var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStroke1.addColorStop(0, '#005bea');  
      gradientStroke1.addColorStop(1, '#00c6fb'); 

  var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: ['Chrome', 'Firefox', 'Safari', 'Opera', 'Edge', 'Mozila', 'Others'],
          datasets: [{
              label: 'Visits',
              data: [60, 50, 40, 30, 20, 25, 15],
              backgroundColor: [
                  gradientStroke1
              ],
              borderColor: [
                  gradientStroke1
              ],
              borderWidth: 0,
              borderRadius: 20
          }]
      },
      options: {
          indexAxis: 'y',
          maintainAspectRatio: false,
          //barPercentage: 0.9,
          categoryPercentage: 0.3,
          plugins: {
              legend: {
                  maxWidth: 20,
                  boxHeight: 20,
                  position:'bottom',
                  display: false,
              }
          },
          scales: {
              x: {
                stacked: false,
                beginAtZero: true
              },
              y: {
                stacked: false,
                beginAtZero: true
              }
            }
      }
  });



// chart7
var ctx = document.getElementById('chart7').getContext('2d');

var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke1.addColorStop(0, '#17ad37');  
    gradientStroke1.addColorStop(1, '#98ec2d');


var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
        datasets: [{
            label: 'Visitors',
            data: [12, 25, 13, 25, 14, 35, 10],
            backgroundColor: [
                gradientStroke1
            ],
             fill: {
                target: 'origin',
                above: 'rgb(23 173 55 / 7%)',   // Area will be red above the origin
                below: 'rgb(23 173 55 / 7%)'    // And blue below the origin
              },
            //tension: 0.4,
            borderColor: [
                gradientStroke1
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
                beginAtZero: false
            }
        }
    }
});





// chart8
var ctx = document.getElementById('chart8').getContext('2d');

var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke1.addColorStop(0, '#005bea');
    gradientStroke1.addColorStop(1, '#00c6fb');

var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke2.addColorStop(0, '#ff6a00');  
    gradientStroke2.addColorStop(1, '#ee0979'); 


var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [ {
            type: 'line',
            label: 'New Visitors',
            data: [0, 25, 12, 35, 20, 38, 13],
            tension: 0.4,
            backgroundColor: [
                gradientStroke2
            ],
            borderColor: [
                gradientStroke2
            ],
        },{
            type: 'line',
            label: 'Old Visitors',
            data: [15, 30, 22, 55, 14, 35, 40],
            tension: 0.4,
            
        }],
        labels: ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
    },
    options: {
        borderRadius: 20,
        categoryPercentage: 0.4,
        maintainAspectRatio: false,
        cutout: 130,
        plugins: {
        legend: {
            display: true,
            position:'bottom',
        }
    }
        
    }
});






  
    
});