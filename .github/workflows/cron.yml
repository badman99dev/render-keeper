name: Ultimate Render Reviver & Auto-Active

on:
  schedule:
    - cron: '*/7 * * * *'  # Har 7 min mein ping karega
  workflow_dispatch: 

jobs:
  ping_and_push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4

      - name: Wake up Render Services
        run: |
          urls=(
            "https://git-workflow-g1ws.onrender.com"
            "https://mantraaibot-1.onrender.com/"
            "https://movie-in-db.onrender.com"
            "https://repair-old-data.onrender.com"
            "https://db-cloning.onrender.com"
            "https://movie-in-db-1.onrender.com"
          )
          for url in "${urls[@]}"; do
            echo "Pinging $url..."
            curl -s -I "$url" | grep "HTTP/" || echo "Failed: $url"
          done

      - name: Auto-Keep-Active (Every 15 Days)
        # Ye step sirf mahine ki 1 aur 15 tarikh ko chalega
        if: github.event_name == 'schedule' && (github.event.schedule == '0 0 1 * *' || github.event.schedule == '0 0 15 * *')
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          echo "Last Active: $(date)" > last_seen.txt
          git add last_seen.txt
          git commit -m "Keep-alive: Periodic activity to prevent workflow suspension"
          git push
