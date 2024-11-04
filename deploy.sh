docker stop etf-portfolio-drawdown 2>/dev/null || true && \
docker rm etf-portfolio-drawdown 2>/dev/null || true && \
docker build --no-cache -t etf-portfolio-drawdown . && \
docker run -d -p 3031:3031 --memory="512m" --name etf-portfolio-drawdown etf-portfolio-drawdown