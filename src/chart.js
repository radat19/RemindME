// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['corechart'] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function draw_chart() {
  var data = new google.visualization.DataTable();
  // classmate_data_processing(classmate_data, data);
  classmate_data_processing(data);


  // Set chart options
  var options = {
    'title': 'Overview',
    'width': 400,
    'height': 300
  };

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}

// model of MVC
// function classmate_data_processing(input_data,){
function bill_data_processing(result_data) {
  // this function process classmate data and create data table
  var recurring_amt = 0;
  var one_time_amt = 0;

  // Create the data table.
  result_data.addColumn('string', 'Element');
  result_data.addColumn('number', 'Count');
  result_data.addRows([
    ['Recurring', recurring_amt],
    ['One-time Payment', one_time_amt]
  ]);
}
