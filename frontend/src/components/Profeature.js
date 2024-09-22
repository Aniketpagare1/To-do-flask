import React from 'react';

function ProFeature() {
  const handleProPurchase = () => {
    fetch('/create-checkout-session', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: 'user@example.com' }),
    })
      .then(res => res.json())
      .then(data => {
        window.location.href = data.url;  // Redirect to Stripe payment page
      });
  };

  return (
    <div>
      <h1>Get Pro License</h1>
      <button onClick={handleProPurchase}>Buy Pro License ($50)</button>
    </div>
  );
}

export default ProFeature;
