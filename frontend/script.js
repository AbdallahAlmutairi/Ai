async function fetchRecommendation() {
  const symbol = document.getElementById('symbol').value;
  if (!symbol) return;
  const response = await fetch(`/api/recommendation/${symbol}`);
  const data = await response.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);
}
