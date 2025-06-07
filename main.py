from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def landing_page1():
    return """
    <h1>Welcome to Landing Page 1</h1>
    <div style="max-width:900px;margin:30px auto;background:#f8f8f8;border-radius:12px;padding:32px 24px;box-shadow:0 2px 8px rgba(0,0,0,0.07);font-size:0.98em;line-height:1.7;">
        <h2>Top 5 Gaming Phones in 2025</h2>
        <p>
            The ASUS ROG Phone 8 Pro, priced around ₹89,999, is a powerhouse designed for gamers who demand the best. Its 6.78-inch FHD+ AMOLED display supports a 165Hz refresh rate and HDR10+, making every game look stunningly smooth and vibrant. Powered by the Snapdragon 8 Gen 3 and up to 24GB RAM, this phone handles even the most demanding titles with ease. Its 6000mAh battery and 65W fast charging ensure you can play for hours without interruption, while advanced vapor chamber cooling keeps the device running cool. Features like AirTrigger controls, customizable RGB lighting, and dual front-facing speakers create an immersive gaming experience, and WiFi 7 support ensures lag-free online play.
        </p>
        <p>
            The Nubia RedMagic 9 Pro+, with a price tag of about ₹72,999, stands out with its 6.8-inch AMOLED display, 165Hz refresh rate, and an impressive 960Hz touch sampling rate for ultra-responsive controls. Its built-in cooling fan and shoulder triggers are perfect for marathon gaming sessions. With up to 24GB RAM, 1TB storage, and a 6500mAh battery, this phone is built for performance and endurance. The Game Space software allows for deep performance tuning, and the under-display camera and customizable RGB lighting add a futuristic touch that appeals to tech enthusiasts.
        </p>
        <p>
            Apple’s iPhone 15 Pro Max, retailing at ₹1,59,900, brings console-quality gaming to iOS with its A17 Pro chip and 6-core GPU. The 6.7-inch Super Retina XDR OLED display with 120Hz ProMotion and Dolby Vision ensures stunning visuals, while the 48MP triple rear camera and spatial audio enhance both gaming and multimedia experiences. With up to 1TB NVMe storage and MagSafe fast charging, it’s a top choice for gamers who also want a premium all-rounder. Apple Arcade, MetalFX upscaling, and exclusive iOS titles make it a favorite for those invested in the Apple ecosystem.
        </p>
        <p>
            Samsung’s Galaxy S24 Ultra, priced at ₹1,29,999, is a productivity and gaming beast, equipped with a 6.8-inch QHD+ Dynamic AMOLED 2X display, Snapdragon 8 Gen 3 or Exynos 2400 (depending on region), and up to 16GB RAM. Its 5000mAh battery, S Pen support, vapor chamber cooling, and Dolby Atmos speakers make it versatile for both work and play. Game Booster software and DeX mode add to its appeal, while the 200MP quad rear camera ensures you capture every moment in detail.
        </p>
        <p>
            The OnePlus 12, at ₹64,999, rounds out the top five with its 6.82-inch AMOLED display, 120Hz refresh rate, and Snapdragon 8 Gen 3 processor. With up to 16GB RAM, 512GB storage, and a 5400mAh battery supporting 100W fast charging, it offers flagship performance at a competitive price. Features like HyperBoost gaming engine, advanced cooling, and Pro Gaming Mode ensure smooth gameplay, while OxygenOS 14 provides a clean, responsive user experience.
        </p>
        <h2>Choosing the Best Gaming Phone & Trends</h2>
        <p>
            When selecting a gaming phone in 2025, prioritize the latest processors (Snapdragon 8 Gen 3 or Apple A17 Pro), at least 8GB RAM, and high refresh rate AMOLED displays for immersive visuals. Look for advanced cooling systems, large batteries (5000mAh+), and fast charging to support long sessions. Features like shoulder triggers, customizable RGB, and stereo speakers can enhance your experience, while gaming software and accessory support add further value. The trend is moving towards WiFi 7, built-in cooling fans, and AI-based performance tuning. Cloud gaming integration, improved haptics, and immersive audio are also shaping the future of mobile gaming.
        </p>
        <h2>Tips & FAQs for Mobile Gamers</h2>
        <p>
            To get the most out of your gaming phone, keep your device updated, use a quality screen protector and case, and monitor temperatures during long sessions. Adjust in-game settings for optimal performance and battery life, and consider gaming triggers or controllers for competitive play. Take regular breaks to avoid eye strain and fatigue. Most gaming phones are excellent for daily use, offering top-tier cameras and build quality. With proper care, they last as long as any flagship device, though heavy gaming may impact battery health over time. Many support a range of accessories, and if you’re a serious gamer, investing in a gaming phone in 2025 is well worth it.
        </p>
        <p>
            These phones represent the best options for mobile gamers in 2025, offering a mix of raw power, display quality, battery life, and gaming-specific features. Choose the one that fits your needs and budget for the ultimate gaming experience!
        </p>
        <div style="text-align:center;margin-top:40px;">
            <button id="next-btn" style="display:none;background:red;color:white;padding:16px 40px;border-radius:8px;font-size:1.2em;font-weight:bold;cursor:pointer;">Next</button>
        </div>
    </div>
    <script>
        setTimeout(function() {
            document.getElementById('next-btn').style.display = 'inline-block';
        }, 20000);
        document.getElementById('next-btn').onclick = function() {
            window.location.href = '/landing2';
        }
    </script>
    """

@app.get("/landing2", response_class=HTMLResponse)
async def landing_page2():
    return """
    <h1>Welcome to Landing Page 2</h1>
    <div style="max-width:900px;margin:30px auto;background:#f8f8f8;border-radius:12px;padding:32px 24px;box-shadow:0 2px 8px rgba(0,0,0,0.07);font-size:0.98em;line-height:1.7;">
        <h2>Top 5 Best Mutual Funds in India (2025)</h2>
        <p>
            Axis Bluechip Fund is a large-cap mutual fund managed by Axis Mutual Fund, designed for investors seeking long-term capital appreciation. It primarily invests in the top 100 stocks listed in the Indian markets, focusing on stability and growth. As of May 30, 2025, the fund's Net Asset Value (NAV) is ₹59.57, with an expense ratio of 1.57%. The fund holds a diversified portfolio consisting of 94.21% equity, 11.54% debt, and -5.75% cash & cash equivalents. Axis Bluechip Fund aims to outperform inflation and fixed-income investments over a five-year or longer period, though investors should be prepared for market ups and downs. The total asset size of the fund is ₹33,218 crore, representing 8.86% of investments in its category. The fund follows a growth-oriented strategy, meaning profits are reinvested rather than distributed as dividends. It invests predominantly in large-cap companies, which are expected to be less risky compared to mid- and small-cap stocks. Investors can start with a minimum investment of ₹100, and the fund has an exit load of 1% if redeemed within 365 days.
        </p>
        <p>
            Parag Parikh Flexi Cap Fund is a flexi-cap mutual fund managed by PPFAS Mutual Fund, designed for investors seeking long-term capital appreciation. Unlike traditional large-cap or mid-cap funds, this scheme has the flexibility to invest across large-cap, mid-cap, and small-cap stocks, allowing it to adapt to market conditions. As of June 4, 2025, the fund's NAV stands at ₹82.55, with an expense ratio of 1.27%. The fund holds a diversified portfolio consisting of 73.68% equity, 23.89% debt, and 2.43% cash & cash equivalents. The total asset size of the fund is ₹98,541 crore, representing 21.62% of investments in its category. Parag Parikh Flexi Cap Fund follows a growth-oriented strategy, reinvesting profits rather than distributing them as dividends. Investors can start with a minimum investment of ₹1,000, and the fund has an exit load of 2% if redeemed within 365 days. Its flexibility and global exposure make it a popular choice for investors looking for diversification and long-term growth.
        </p>
        <p>
            HDFC Hybrid Equity Fund is an aggressive hybrid mutual fund managed by HDFC Mutual Fund, designed for investors seeking long-term capital appreciation with a mix of equity and debt investments. The fund primarily invests 65-80% in equity and the remaining portion in debt and money market instruments, aiming to balance growth potential with stability. As of June 4, 2025, the fund's Net Asset Value (NAV) stands at ₹117.97, with an expense ratio of 1.69%. It has a very high risk rating, making it suitable for investors with a long-term horizon who can tolerate market fluctuations. The total asset size of the fund is ₹23,851 crore, representing 10.55% of investments in its category. The fund follows a growth-oriented strategy, meaning profits are reinvested rather than distributed as dividends. Investors can start with a minimum investment of ₹100, and the fund has an exit load of 1% if redeemed within 365 days. The fund aims to maintain a diversified portfolio, investing across market capitalizations to optimize returns while managing risk.
        </p>
        <p>
            Mirae Asset Large Cap Fund is a large-cap equity mutual fund managed by Mirae Asset Mutual Fund. It is known for its consistent performance and focus on sustainable growth companies with strong fundamentals and robust corporate governance. As of June 2025, the fund's NAV is ₹92.34, with an expense ratio of 1.60%. The fund invests primarily in large-cap stocks, offering a diversified portfolio that includes major holdings like HDFC Bank, ICICI Bank, Reliance Industries, and Infosys. Mirae Asset Large Cap Fund is suitable for investors seeking steady growth with moderate risk, and it has a proven track record of outperforming its benchmark over the long term.
        </p>
        <p>
            SBI Small Cap Fund is a small-cap equity mutual fund managed by SBI Mutual Fund, ideal for aggressive investors seeking high growth potential over the long term. The fund invests in emerging businesses with high growth potential, though it comes with higher volatility and risk. As of June 2025, the fund's NAV is ₹134.21, with an expense ratio of 1.70%. The total asset size is ₹18,500 crore, and the fund holds a diversified portfolio of small-cap stocks, including Elgi Equipments, Blue Star, and Hawkins Cookers. SBI Small Cap Fund is best suited for investors with a high risk appetite and a long-term investment horizon.
        </p>
        <h2>How to Choose & Invest in Mutual Funds</h2>
        <p>
            When choosing a mutual fund, define your investment goal—whether it's wealth creation, tax saving, or regular income. Assess your risk appetite: equity funds offer higher returns but come with more risk, while hybrid and debt funds are safer but yield moderate returns. Always check the fund's long-term performance, expense ratio, and the track record of the fund manager. Diversification is key to reducing risk, and tax efficiency can be achieved through ELSS funds. Open-ended funds provide liquidity, but be mindful of exit loads and lock-in periods. SIPs (Systematic Investment Plans) are a great way to invest regularly and benefit from compounding.
        </p>
        <h2>Trends, Tips & FAQs</h2>
        <p>
            In 2025, Indian investors are increasingly turning to passive and index funds, as well as international and ESG (Environmental, Social, Governance) options. Technology and robo-advisors are making portfolio management easier, and SIP inflows continue to rise. To maximize returns, start investing early, review your portfolio annually, and avoid chasing past returns. Understand all costs, tax implications, and stay invested for the long term. Mutual funds are regulated by SEBI and are generally safe, but returns are subject to market risks. SIPs allow for regular, disciplined investing, and most open-ended funds offer easy withdrawal, though you should check for exit loads and lock-in periods. Taxation depends on the type of fund and holding period, and direct plans usually offer higher returns due to lower expense ratios.
        </p>
        <p>
            These mutual funds represent some of the best options for Indian investors in 2025, balancing risk and reward across different categories. Always consult a financial advisor and read scheme documents before investing. Mutual funds are subject to market risks. Read all scheme-related documents carefully before investing. Past performance is not indicative of future results.
        </p>
        <div style="text-align:center;margin-top:40px;">
            <button id="next-btn" style="display:none;background:red;color:white;padding:16px 40px;border-radius:8px;font-size:1.2em;font-weight:bold;cursor:pointer;">Back</button>
        </div>
    </div>
    <script>
        setTimeout(function() {
            document.getElementById('next-btn').style.display = 'inline-block';
        }, 20000);
        document.getElementById('next-btn').onclick = function() {
            window.location.href = '/';
        }
    </script>
    """