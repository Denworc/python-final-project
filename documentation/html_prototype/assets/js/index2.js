$(function() {
    "use strict";
	
	// chart 1
	$('#dash2-chart-1').sparkline([5,8,7,10,9,10,8,6,4,6,8,7,6,8], {
            type: 'bar',
            height: '35',
            barWidth: '3',
            resize: true,
            barSpacing: '3',
            barColor: '#fff'
        });

    
	// chart 2
    $("#dash2-chart-2").sparkline([0,5,3,7,5,10,3,6,5,10], {
            type: 'line',
            width: '80',
            height: '40',
            lineWidth: '2',
            lineColor: '#fff',
            fillColor: 'transparent',
            spotColor: '#fff',
        })
		
		
	// chart 3
     $("#dash2-chart-3").sparkline([2,3,4,5,4,3,2,3,4,5,6,5,4,3,4,5], {
        type: 'discrete',
        width: '75',
        height: '40',
        lineColor: '#fff',
        lineHeight: 22

     });	
		

	// chart 4	
	$("#dash2-chart-4").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
		type: 'line',
		width: '100',
		height: '25',
		lineWidth: '2',
		lineColor: '#ffffff',
		fillColor: 'transparent'
		
	});
	

// chart 5
 var ctx = document.getElementById('dash2-chart-5').getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: [1, 2, 3, 4, 5, 6, 7, 8],
          datasets: [{
            label: 'Classique',
            data: [30, 20, 45, 55, 30, 45, 10, 30],
            pointBorderWidth: 2,
            pointBackgroundColor: 'transparent',
			pointHoverBackgroundColor: '#008cff',
            backgroundColor: '#008cff',
            borderColor: '#008cff',
            borderWidth: 2
          }, {
            label: 'Critique',
            data: [70, 50, 85, 60, 95, 75, 50, 80],
            pointBorderWidth: 2,
            pointBackgroundColor: 'transparent',
			pointHoverBackgroundColor: '#c60000',
            backgroundColor: '#c60000',
            borderColor: '#c60000',
            borderWidth: 2
          }]
        },
        options: {
            legend: {
              display: true,
			  labels: {
                boxWidth:40
              }
            },
            tooltips: {
			  displayColors:false
            }

         }
      });


  // chart 6
    var ctx = document.getElementById("dash2-chart-6").getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: [1, 2, 3, 4, 5, 6, 7, 8],
          datasets: [{
            label: 'Jour',
            data: [40, 30, 60, 35, 60, 25, 50, 40],
            borderColor: '#003783',
            backgroundColor: '#003783',
            hoverBackgroundColor: '#003783',
            pointRadius: 0,
            fill: false,
            borderWidth: 1
          }, {
            label: 'Nuit',
            data: [50, 60, 40, 70, 35, 75, 30, 20],
            borderColor: '#454545',
            backgroundColor: '#454545',
            hoverBackgroundColor: '#454545',
            pointRadius: 0,
            fill: false,
            borderWidth: 1
          }]
        },
		options:{
		  legend: {
			  position: 'bottom',
              display: true,
			  labels: {
                boxWidth:12
              }
            },
			tooltips: {
			  displayColors:false,
			},	
		  scales: {
			  xAxes: [{
				barPercentage: .5
			  }]
		     }
		}
      });
	  
	  
	  
	  
// chart 7
 var ctx = document.getElementById('dash2-chart-7').getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: [1, 2, 3, 4, 5, 6, 7],
          datasets: [{
            label: 'Alertes',
            data: [3, 30, 10, 10, 22, 12, 5],
            pointBorderWidth: 2,
            pointHoverBackgroundColor: '#C60000',
            backgroundColor: '#C60000',
            borderColor: 'transparent',
            borderWidth: 1
          }]
        },
        options: {
            legend: {
			  position: 'bottom',
              display:false
            },
            tooltips: {
			  displayColors:false,	
              mode: 'nearest',
              intersect: false,
              position: 'nearest',
              xPadding: 10,
              yPadding: 10,
              caretPadding: 10
            },
			scales: {
			  xAxes: [{
				ticks: {
                    beginAtZero:true
                },
				gridLines: {
				  display: true 
				},
			  }],
			   yAxes: [{
				ticks: {
                    beginAtZero:true
                },
				gridLines: {
				  display: true 
				},
			  }]
		     }

         }
      });  
	  
	  
	  

// worl map

jQuery('#dashboard-map').vectorMap(
{
    map: 'world_mill_en',
    backgroundColor: 'transparent',
    borderColor: '#818181',
    borderOpacity: 0.25,
    borderWidth: 1,
    zoomOnScroll: false,
    color: '#009efb',
    regionStyle : {
        initial : {
          fill : '#15ca20'
        }
      },
    markerStyle: {
      initial: {
                    r: 9,
                    'fill': '#fff',
                    'fill-opacity':1,
                    'stroke': '#000',
                    'stroke-width' : 5,
                    'stroke-opacity': 0.4
                },
                },
    enableZoom: true,
    hoverColor: '#009efb',
    markers : [{
        latLng : [21.00, 78.00],
        name : 'I Love My India'
      
      }],
    hoverOpacity: null,
    normalizeFunction: 'linear',
    scaleColors: ['#b6d6ff', '#005ace'],
    selectedColor: '#c9dfaf',
    selectedRegions: [],
    showTooltip: true
});

  // chart 8
  $("#dash2-chart-8").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#dd4b39',
            fillColor: 'rgba(221, 75, 57, 0.5)',
            spotColor: '#dd4b39',
    }); 
	
	
	// chart 9
	$("#dash2-chart-9").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#3b5998',
            fillColor: 'rgba(59, 89, 152, 0.5)',
            spotColor: '#3b5998',
    });
	
	// chart 10
	$("#dash2-chart-10").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#55acee',
            fillColor: 'rgba(85, 172, 238, 0.5)',
            spotColor: '#55acee',
    });
	
	
	// chart 11
	$("#dash2-chart-11").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#0976b4',
            fillColor: 'rgba(9, 118, 180, 0.5)',
            spotColor: '#0976b4',
    });
	
	
	// chart 12
	$("#dash2-chart-12").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#1769ff',
            fillColor: 'rgba(23, 105, 255, 0.5)',
            spotColor: '#1769ff',
    });
	
	
	// chart 13
	$("#dash2-chart-13").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#ea4c89',
            fillColor: 'rgba(234, 76, 137, 0.5)',
            spotColor: '#ea4c89',
    });
	
	
	// chart 14
	$("#dash2-chart-14").sparkline([3,5,3,7,5,10,3,6,5,7], {
            type: 'line',
            width: '100',
            height: '20',
            lineWidth: '2',
            lineColor: '#333333',
            fillColor: 'rgba(51, 51, 51, 0.5)',
            spotColor: '#333333',
    });

	
	// chart 15
   $('#dash2-chart-15').sparkline([5,8,7,10,9,10,8,6,4,6,8,7,6,8,10,8,6,4], {
            type: 'bar',
            height: '45',
            barWidth: '3',
            resize: true,
            barSpacing: '5',
            barColor: '#fff'
        });	
	

  // chart 16
  var ctx = document.getElementById("dash2-chart-16").getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["Critique", "Classique", "Divers"],
          datasets: [{
            backgroundColor: [
              '#b81cff',
              '#0dceec',
              '#fd3550'
            ],

             hoverBackgroundColor: [
              '#b81cff',
              '#0dceec',
              '#fd3550'
            ],

            data: [50, 50, 50]
          }]
        },
        options: {
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });


  // chart 17
  var ctx = document.getElementById("dash2-chart-17").getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
          labels: ["Gross Profit", "Revenue", "Expense"],
          datasets: [{
            backgroundColor: [
              '#15ca20',
              '#008cff',
              '#fd3550'
            ],

             hoverBackgroundColor: [
              '#15ca20',
              '#008cff',
              '#fd3550'
            ],
            data: [5, 8, 7]
          }]
        },
        options: {
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });


	  
  // chart 18
  var ctx = document.getElementById("dash2-chart-18").getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["Jeans", "T-Shirts", "Shoes"],
          datasets: [{
            backgroundColor: [
              '#fd3550',
              '#ff9700',
              '#223035'
            ],
            hoverBackgroundColor: [
              '#fd3550',
              '#ff9700',
              '#223035'
            ],
            data: [25, 25, 25]
          }]
        },
        options: {
            legend: {
              display: false
            },
            tooltips: {
			  displayColors:false
            }
        }
      });
	  
});


 // Index Notification
	 
	 function info_noti(){
		Lobibox.notify('info', {
		pauseDelayOnHover: true,
		continueDelayOnInactiveTab: false,
		size: 'mini',
		position: 'top right',
		icon: 'fa fa-info-circle',
		msg: 'This is Solid Color Dashboard'
		});
	  } 