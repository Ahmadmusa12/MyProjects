function encrypt() {
  const input = document.getElementById('input').value;
  let encrypted = '';
  
  for (let i = 0; i < input.length; i++) {
    encrypted += String.fromCharCode(input.charCodeAt(i) + 5);
  }

  document.getElementById('output').textContent = encrypted;
}
