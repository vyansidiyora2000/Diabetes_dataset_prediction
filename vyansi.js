// Sample array of objects
const data = [
    { name: 'Alice', age: 25, score: 90 },
    { name: 'Bob', age: 30, score: 85 },
    { name: 'Charlie', age: 28, score: 95 },
    { name: 'David', age: 35, score: 88 },
  ];
  
  // Filter the array (e.g., age greater than 28)
  const filteredData = data.filter(item => item.age > 28);
  
  // Sort the array based on a property (e.g., sort by score in descending order)
  const sortedData = filteredData.sort((a, b) => b.score - a.score);
  
  // Display the result
  console.log(sortedData);
  