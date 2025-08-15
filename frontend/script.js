async function fetchRecommendation(symbolInput) {
  const symbol =
    typeof symbolInput === 'string'
      ? symbolInput
      : document.getElementById('symbol').value;
  if (!symbol) return;
  const response = await fetch(`/api/recommendation/${symbol}`);
  const data = await response.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);
}

async function loadWatchlist() {
  const res = await fetch('/api/watchlist');
  const data = await res.json();
  const list = document.getElementById('watchlist');
  list.innerHTML = '';
  data.symbols.forEach((sym) => {
    const li = document.createElement('li');
    li.textContent = sym;
    li.style.cursor = 'pointer';
    li.onclick = () => fetchRecommendation(sym);
    const del = document.createElement('button');
    del.textContent = 'x';
    del.style.marginLeft = '0.5rem';
    del.onclick = async (e) => {
      e.stopPropagation();
      await fetch(`/api/watchlist/${sym}`, { method: 'DELETE' });
      loadWatchlist();
    };
    li.appendChild(del);
    list.appendChild(li);
  });
}

async function addToWatchlist() {
  const symbol = document.getElementById('watch-symbol').value;
  if (!symbol) return;
  await fetch(`/api/watchlist/${symbol}`, { method: 'POST' });
  document.getElementById('watch-symbol').value = '';
  loadWatchlist();
}

async function updateRiskProfile() {
  const profile = document.getElementById('risk-profile').value;
  await fetch(`/api/risk-profile/${profile}`, { method: 'POST' });
}

async function init() {
  // Load initial state
  const res = await fetch('/api/risk-profile');
  const data = await res.json();
  document.getElementById('risk-profile').value = data.risk_profile;
  loadWatchlist();
}

window.onload = init;
