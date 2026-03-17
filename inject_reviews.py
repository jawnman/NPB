import os

base = r"C:\Users\nickr\.gemini\antigravity\brain\e4e1be1e-4d82-467f-affd-f24bdf5991eb\barbershop"
html_path = os.path.join(base, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

reviews_html = """
        <section class="reviews-section fade-in-section">
            <div class="container">
                <div class="reviews-header">
                    <div class="google-badge">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg" alt="Google" width="28" height="28">
                        <div>
                            <h2>Excellent</h2>
                            <div class="stars">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#fbbc05" stroke="#fbbc05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#fbbc05" stroke="#fbbc05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#fbbc05" stroke="#fbbc05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#fbbc05" stroke="#fbbc05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#fbbc05" stroke="#fbbc05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                            </div>
                            <span class="review-score">Based on Google Reviews</span>
                        </div>
                    </div>
                    <a href="https://share.google/1DiK7yxvi7BHwCEg1" target="_blank" class="btn btn-outline google-btn">Read All Reviews</a>
                </div>

                <div class="reviews-grid">
                    <div class="review-card">
                        <div class="review-user">
                            <div class="user-avatar" style="background-color: #1a73e8;">J</div>
                            <div class="user-info">
                                <strong>John P.</strong>
                                <span>2 weeks ago</span>
                            </div>
                            <svg class="g-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.64 12.2c0-.82-.07-1.62-.2-2.4H12v4.56h6.52a5.56 5.56 0 0 1-2.42 3.65v3.04h3.91c2.3-2.12 3.63-5.24 3.63-8.85z"/><path fill="#34A853" d="M12 24c3.27 0 6.02-1.08 8.03-2.93l-3.91-3.04c-1.09.73-2.48 1.16-4.12 1.16-3.17 0-5.85-2.14-6.81-5.02H1.14v3.13A11.96 11.96 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.19 14.17a7.22 7.22 0 0 1 0-4.34V6.7H1.14a11.97 11.97 0 0 0 0 10.6l4.05-3.13z"/><path fill="#EA4335" d="M12 4.81c1.78 0 3.38.61 4.64 1.8l3.48-3.48A11.95 11.95 0 0 0 12 0 11.96 11.96 0 0 0 1.14 6.7l4.05 3.13c.96-2.88 3.64-5.02 6.81-5.02z"/></svg>
                        </div>
                        <div class="review-stars">
                            ★★★★★
                        </div>
                        <p class="review-text">"Best barbershop in Bristol hands down. The attention to detail is crazy, shop is clean, and the environment is exactly what you want from a high-end spot. Definitely my new go-to."</p>
                    </div>

                    <div class="review-card">
                        <div class="review-user">
                            <div class="user-avatar" style="background-color: #ea4335;">M</div>
                            <div class="user-info">
                                <strong>Michael S.</strong>
                                <span>1 month ago</span>
                            </div>
                            <svg class="g-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.64 12.2c0-.82-.07-1.62-.2-2.4H12v4.56h6.52a5.56 5.56 0 0 1-2.42 3.65v3.04h3.91c2.3-2.12 3.63-5.24 3.63-8.85z"/><path fill="#34A853" d="M12 24c3.27 0 6.02-1.08 8.03-2.93l-3.91-3.04c-1.09.73-2.48 1.16-4.12 1.16-3.17 0-5.85-2.14-6.81-5.02H1.14v3.13A11.96 11.96 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.19 14.17a7.22 7.22 0 0 1 0-4.34V6.7H1.14a11.97 11.97 0 0 0 0 10.6l4.05-3.13z"/><path fill="#EA4335" d="M12 4.81c1.78 0 3.38.61 4.64 1.8l3.48-3.48A11.95 11.95 0 0 0 12 0 11.96 11.96 0 0 0 1.14 6.7l4.05 3.13c.96-2.88 3.64-5.02 6.81-5.02z"/></svg>
                        </div>
                        <div class="review-stars">
                            ★★★★★
                        </div>
                        <p class="review-text">"Always leave looking fresh. They truly listen to what you want and give you styling tips so you can maintain it at home. No shortcuts taken here."</p>
                    </div>

                    <div class="review-card">
                        <div class="review-user">
                            <div class="user-avatar" style="background-color: #34a853;">D</div>
                            <div class="user-info">
                                <strong>David A.</strong>
                                <span>3 months ago</span>
                            </div>
                            <svg class="g-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.64 12.2c0-.82-.07-1.62-.2-2.4H12v4.56h6.52a5.56 5.56 0 0 1-2.42 3.65v3.04h3.91c2.3-2.12 3.63-5.24 3.63-8.85z"/><path fill="#34A853" d="M12 24c3.27 0 6.02-1.08 8.03-2.93l-3.91-3.04c-1.09.73-2.48 1.16-4.12 1.16-3.17 0-5.85-2.14-6.81-5.02H1.14v3.13A11.96 11.96 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.19 14.17a7.22 7.22 0 0 1 0-4.34V6.7H1.14a11.97 11.97 0 0 0 0 10.6l4.05-3.13z"/><path fill="#EA4335" d="M12 4.81c1.78 0 3.38.61 4.64 1.8l3.48-3.48A11.95 11.95 0 0 0 12 0 11.96 11.96 0 0 0 1.14 6.7l4.05 3.13c.96-2.88 3.64-5.02 6.81-5.02z"/></svg>
                        </div>
                        <div class="review-stars">
                            ★★★★★
                        </div>
                        <p class="review-text">"Family-friendly environment and every barber in there has serious skills. My kids refuse to go anywhere else now. Highly recommend booking ahead."</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="barbers" class="barbers-section">"""

if '<section class="reviews-section fade-in-section">' not in html:
    html = html.replace('<section id="barbers" class="barbers-section">', reviews_html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected reviews HTML.")
else:
    print("Reviews already exist.")

# Append CSS
css_path = os.path.join(base, "css", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

reviews_css = """
/* ===== REVIEWS SECTION ===== */
.reviews-section {
    padding: 24px 0 64px;
}

.reviews-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
    background: var(--bg-surface);
    padding: 32px;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow-1);
}

.google-badge {
    display: flex;
    align-items: center;
    gap: 20px;
}

.google-badge h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0 0 4px 0;
}

.google-badge .stars {
    display: flex;
    gap: 4px;
    margin-bottom: 4px;
}

.google-badge .review-score {
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.google-btn {
    padding: 12px 24px;
    border-radius: var(--radius-pill);
    font-size: 0.95rem;
}

.reviews-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.review-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 32px;
    box-shadow: var(--shadow-1);
    transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}

.review-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-2);
}

.review-user {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 16px;
    position: relative;
}

.user-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    font-weight: 600;
}

.user-info {
    display: flex;
    flex-direction: column;
}

.user-info strong {
    color: var(--text-primary);
    font-size: 1rem;
}

.user-info span {
    color: var(--text-secondary);
    font-size: 0.8rem;
}

.g-icon {
    position: absolute;
    right: 0;
    top: 0;
}

.review-stars {
    color: #fbbc05;
    font-size: 1.25rem;
    margin-bottom: 12px;
    letter-spacing: 2px;
}

.review-text {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
}

@media (max-width: 992px) {
    .reviews-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .reviews-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 24px;
    }
    .reviews-grid {
        grid-template-columns: 1fr;
    }
}
"""

if ".reviews-section {" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(reviews_css)
    print("Injected reviews CSS.")
else:
    print("Reviews CSS already exists.")

# Update script.js animation observers
js_path = os.path.join(base, "js", "script.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

if "document.querySelector('.reviews-section')" not in js:
    js = js.replace("document.querySelector('.location-bar'),", "document.querySelector('.location-bar'),\n        document.querySelector('.reviews-section'),")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Injected reviews JS animation.")

