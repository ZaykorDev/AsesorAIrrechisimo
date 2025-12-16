# Features Guide

Complete overview of all features in El Asesor AIrrecho.

## Chat Interface

### Natural Language Interaction

Ask questions in plain Spanish about your portfolio, market trends, or specific investments.

**Examples:**
- "¿Cómo está mi portafolio?"
- "¿Debería comprar más AAPL?"
- "¿Qué opinas de VTI?"
- "¿Hay algún riesgo en mis holdings?"
- "Investiga TSM"

### Real-Time Web Search

The AI automatically searches the web for current information:
- Stock prices and performance
- Analyst ratings and price targets
- Recent news and earnings reports
- Market trends and economic indicators
- Company fundamentals

**How it works:**
1. You ask a question
2. AI determines if current data is needed
3. Searches web automatically
4. Synthesizes information
5. Provides personalized recommendation

### Context-Aware Responses

The AI remembers:
- Your risk profile (conservative, moderate, aggressive)
- Your portfolio holdings
- Previous conversation context
- Your investment goals

This allows for coherent multi-turn conversations:
```
You: "What's VTI?"
AI: [Explains VTI]

You: "Should I buy it?"
AI: [Knows you're still talking about VTI, gives personalized advice]
```

### Conversation History

- Last 10 messages retained for context
- Clear history button to start fresh
- Chat persists during session
- Resets when browser closes

## Portfolio Management

### Add Holdings

Track multiple types of investments:
- **ETFs** (Exchange-Traded Funds)
- **Stocks** (Individual companies)
- **Bonds** (Fixed income securities)
- **Mutual Funds**

**Information tracked:**
- Symbol/Ticker (e.g., VTI, AAPL)
- Name (e.g., Vanguard Total Stock Market)
- Asset Type
- Quantity/Shares
- Average Purchase Price
- Notes (optional)
- Date Added

### Portfolio Visualization

**Metrics Displayed:**
- Total number of holdings
- Total portfolio value
- Count by asset type (ETFs, Stocks, Bonds)

**Asset Allocation Chart:**
- Visual breakdown by type
- Bar chart showing distribution
- Helps identify concentration risk

### Portfolio Operations

**Edit Holdings:**
- View all holdings in table format
- See quantity, price, total value
- Sort and filter (coming soon)

**Remove Holdings:**
- Select from dropdown
- One-click removal
- Confirmation dialog

**Export Portfolio:**
- Download as CSV file
- Includes all data fields
- Date-stamped filename
- Use for backups or external analysis

**Import Portfolio:**
- Upload CSV file
- Bulk add holdings
- See [example_portfolio.csv](../examples/example_portfolio.csv) for format

## Quick Analysis

One-click analysis buttons provide instant insights.

### Risk Assessment

Analyzes portfolio risk level:
- Diversification score
- Asset allocation review
- Concentration risk identification
- Alignment with risk profile
- Specific recommendations

**Sample Output:**
```
"Tu portafolio tiene 70% en acciones y 30% en bonos. Para un 
perfil conservador, eso está un poco arriesgado chamo. Te 
recomiendo mover 10% de acciones a bonos para llegar a 60/40..."
```

### Sector Analysis

Reviews sector exposure:
- Which sectors you're invested in
- Overweight/underweight areas
- Sector concentration risk
- Diversification opportunities

**What it checks:**
- Technology exposure
- Financial sector weight
- Healthcare allocation
- International vs. domestic
- Growth vs. value

### Top Performers

Identifies best performing holdings:
- Recent price performance
- Year-to-date gains
- Analyst ratings
- News and catalysts
- Comparison to benchmarks

**Includes:**
- Price changes (daily, weekly, monthly)
- Percentage gains
- Volume and momentum
- Recommendation (hold, take profits, add more)

### Rebalancing Recommendations

Suggests portfolio adjustments:
- Which positions to trim
- Where to add exposure
- Target allocation percentages
- Specific action steps
- Reasoning for each change

**Based on:**
- Your risk profile
- Current market conditions
- Diversification principles
- Your investment goals

### Future Outlook

Market predictions and analysis:
- Economic indicators
- Federal Reserve policy
- Sector trends
- Geopolitical factors
- Impact on your specific holdings

**Researches:**
- Upcoming earnings
- Economic reports schedule
- Central bank meetings
- Industry trends
- Analyst forecasts

### Risk Warnings

Identifies potential concerns:
- Negative news about holdings
- Downgrade alerts
- Earnings misses
- Regulatory issues
- Market-wide risks

**Checks for:**
- Stock-specific bad news
- Sector headwinds
- Economic warning signs
- Overvaluation concerns
- Liquidity issues

## Configuration

### Risk Profile

Choose from predefined or custom:

**Conservative:**
- Low volatility preference
- Capital preservation focus
- Higher bond allocation
- Dividend-paying stocks
- Established companies

**Moderate:**
- Balanced approach
- Growth + income
- Mix of stocks and bonds
- Some international exposure
- Moderate risk tolerance

**Aggressive:**
- High growth focus
- Higher volatility acceptance
- Stock-heavy allocation
- Emerging markets
- Growth stocks

**Custom:**
- Describe your own preferences
- AI adapts recommendations
- Mix and match strategies
- Example: "Want 50% stable dividends, 30% growth, 20% bonds"

### API Key Management

- Enter in sidebar
- Stored in session only
- Never saved to disk
- Required for each session
- Easy to update

### Session Management

**Clear Chat History:**
- Removes conversation context
- Starts fresh conversation
- Portfolio data remains
- Useful when changing topics

**Reset All:**
- Clear portfolio
- Clear chat history
- Reset risk profile
- Start completely fresh

## AI Personality Features

### Venezuelan Expressions

Uses authentic Venezuelan slang:
- **chamo/chama** - friend
- **vale** - okay
- **pana** - buddy
- **arrecho** - awesome/impressive
- **coño** - expression of surprise
- **verga** - emphasis
- **burda de** - a lot of
- **chevere** - cool/nice

### Cultural References

Compares everything to Venezuelan experiences:
- "Después de la hiperinflación venezolana..."
- "Más estable que... bueno, nada en Venezuela"
- "Como manejar en la autopista de Caracas"
- "Más diversificado que una hallaca"

### Humor Styles

**Self-deprecating:**
- References Venezuela's economic struggles
- Makes light of difficult situations
- Puts market volatility in perspective

**Sarcastic:**
- Ironic comments about obvious things
- Playful jabs at bad decisions (constructive)
- Witty observations about market behavior

**Encouraging:**
- Celebrates good decisions
- Provides positive reinforcement
- Makes investing less intimidating

### Professional Balance

Despite the humor, analysis remains:
- Factually accurate
- Based on current data
- Considers risk factors
- Provides actionable advice
- References credible sources

## Web Search Integration

### Automatic Research

The AI decides when to search based on:
- Question type
- Need for current data
- Age of information
- Relevance to holdings

### Search Capabilities

**Market Data:**
- Real-time stock prices
- Index levels (S&P 500, Nasdaq, Dow)
- Currency exchange rates
- Commodity prices

**Company Information:**
- Earnings reports
- Analyst ratings
- Price targets
- News and press releases
- Financial metrics

**Economic Indicators:**
- Inflation data
- Employment numbers
- GDP growth
- Interest rates
- Consumer sentiment

### Source Quality

Prioritizes reliable sources:
- Bloomberg
- Reuters
- CNBC
- Yahoo Finance
- Company investor relations
- Federal Reserve
- Government data

## Data Export/Import

### CSV Export

**Includes:**
- All portfolio holdings
- Current valuations
- Purchase information
- Notes and metadata
- Date exported

**Use cases:**
- Backup before updates
- Share with financial advisor
- Track over time
- Import to spreadsheet
- Tax preparation

### CSV Import

**Features:**
- Bulk add holdings
- Update existing holdings
- Validate data format
- Error reporting
- See example format

**Required fields:**
- symbol
- name
- type
- quantity
- avg_price

## Security Features

### Data Privacy

- No data sent to third parties (except Claude API for analysis)
- Portfolio data stays local
- No user accounts or authentication
- No tracking or analytics
- API keys not logged

### Safe API Key Handling

- Session-only storage
- Never written to disk
- Not included in error logs
- Cleared on browser close
- .gitignore protection

### Secure Recommendations

The AI:
- Disclaims it's not a licensed advisor
- Recommends consulting professionals
- Doesn't make guarantees
- Provides educational information
- Emphasizes user responsibility

## User Interface

### Responsive Design

- Works on desktop browsers
- Tablet-friendly
- Mobile-compatible (with limitations)
- Dark mode support (via Streamlit)

### Intuitive Layout

**Three main tabs:**
1. Chat - Conversation interface
2. Portfolio - Holdings management
3. Analysis - Quick insights

**Sidebar:**
- Configuration options
- API key input
- Risk profile selector
- Quick actions

### Visual Feedback

- Loading spinners during AI processing
- Success/error messages
- Color-coded status indicators
- Progress bars for long operations

## Performance

### Optimizations

- Session state for fast access
- Minimal API calls
- Efficient data structures
- Lazy loading
- Cached computations

### Response Times

**Typical speeds:**
- Simple questions: 2-5 seconds
- Web search queries: 5-10 seconds
- Portfolio analysis: 3-7 seconds
- Quick analysis: 5-15 seconds

**Factors affecting speed:**
- API response time
- Web search complexity
- Number of holdings
- Conversation length
- Network latency

---

## Coming Soon

Features in development:
- [ ] Historical performance tracking
- [ ] Multiple portfolio support
- [ ] Broker API integration
- [ ] Mobile app
- [ ] Email alerts
- [ ] Tax-loss harvesting
- [ ] Benchmark comparisons
- [ ] Goal-based planning

---

**Want a feature?** Open an issue on GitHub!