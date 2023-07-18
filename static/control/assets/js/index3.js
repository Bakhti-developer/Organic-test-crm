$(function() {

   


// chart1
var ctx = document.getElementById('chart1').getContext('2d');

var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke1.addColorStop(0, '#005bea');
    gradientStroke1.addColorStop(1, '#00c6fb');

var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke2.addColorStop(0, '#ff6a00');  
    gradientStroke2.addColorStop(1, '#ee0979'); 


var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        datasets: [{
            label: 'Sales',
            data: [10, 25, 18, 35, 20, 38, 23, 26, 15, 32, 20, 13],
            tension: 0.4,
            backgroundColor: [
                gradientStroke1
            ],
            borderColor: [
                gradientStroke1
            ],
            borderWidth: 0,
           
        },{
            label: 'Visits',
            data: [15, 30, 22, 55, 14, 35, 20, 35, 20, 15, 18, 5],
            tension: 0.4,
            backgroundColor: [
                gradientStroke2
            ],
            borderColor: [
                gradientStroke2
            ],
            borderWidth: 3,

            fill: {
                target: 'origin',
                above: 'rgb(238 9 121 / 5%)',   // Area will be red above the origin
                below: 'rgb(238 9 121 / 5%)'    // And blue below the origin
              },
            
        }],
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    options: {
        borderRadius: 30,
        categoryPercentage: 0.3,
        maintainAspectRatio: false,
        //cutout: 130,
        plugins: {
        legend: {
            display: true,
            position:'bottom',
        }
    }
        
    }
});






// chart2
var ctx = document.getElementById('chart2').getContext('2d');

var gradientStroke1 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke1.addColorStop(0, '#005bea');
    gradientStroke1.addColorStop(1, '#00c6fb');

var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke2.addColorStop(0, '#ff6a00');  
    gradientStroke2.addColorStop(1, '#ee0979'); 

var gradientStroke3 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke3.addColorStop(0, '#17ad37');  
    gradientStroke3.addColorStop(1, '#98ec2d'); 

var gradientStroke4 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke4.addColorStop(0, '#7928ca');  
    gradientStroke4.addColorStop(1, '#ff0080'); 

var gradientStroke5 = ctx.createLinearGradient(0, 0, 0, 300);
    gradientStroke5.addColorStop(0, '#f7971e');  
    gradientStroke5.addColorStop(1, '#ffd200'); 

var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Electronics', 'Furniture', 'Fashion', 'Accessories', 'Mobiles'],
        datasets: [{
            data: [155, 120, 110, 150, 90],
            backgroundColor: [
                gradientStroke1,
                gradientStroke2,
                gradientStroke3,
                gradientStroke4,
                gradientStroke5,
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        cutout: 105,
        plugins: {
        legend: {
            display: false,
        }
    }
        
    }
});





// chart3
var ctx = document.getElementById('chart3').getContext('2d');

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
        cutout: 105,
        plugins: {
        legend: {
            display: false,
        }
    }
        
    }
});





      
    
});