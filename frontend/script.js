async function fetchRecommendation(symbolInput) {
  const symbol =
    typeof symbolInput === 'string'
      ? symbolInput
      : document.getElementById('symbol').value.trim();
  if (!symbol) return;
  try {
    const response = await fetch(`/api/recommendation/${symbol}`);
    if (!response.ok) throw new Error('failed to fetch recommendation');
    const data = await response.json();
    document.getElementById('result').textContent = JSON.stringify(
      data,
      null,
      2,
    );
  } catch (err) {
    document.getElementById('result').textContent = err.message;
  }
}

async function loadWatchlist() {
  try {
    const res = await fetch('/api/watchlist');
    if (!res.ok) throw new Error('failed to load watchlist');
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
  } catch (err) {
    document.getElementById('result').textContent = err.message;
  }
}

async function addToWatchlist() {
  const input = document.getElementById('watch-symbol');
  const symbol = input.value.trim().toUpperCase();
  if (!symbol) return;
  try {
    await fetch(`/api/watchlist/${symbol}`, { method: 'POST' });
    input.value = '';
    loadWatchlist();
  } catch (err) {
    document.getElementById('result').textContent = err.message;
  }
}

async function updateRiskProfile() {
  const profile = document.getElementById('risk-profile').value;
  try {
    await fetch(`/api/risk-profile/${profile}`, { method: 'POST' });
  } catch (err) {
    document.getElementById('result').textContent = err.message;
  }
}

async function init() {
  try {
    // Load initial state
    const res = await fetch('/api/risk-profile');
    if (!res.ok) throw new Error('failed to fetch risk profile');
    const data = await res.json();
    document.getElementById('risk-profile').value = data.risk_profile;
    loadWatchlist();
  } catch (err) {
    document.getElementById('result').textContent = err.message;
  }
}

window.onload = init;

