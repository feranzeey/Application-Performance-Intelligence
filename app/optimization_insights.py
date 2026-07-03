# Sample metrics collected from Locust
avg_response_time = 2176  # milliseconds
failure_rate = 0          # percent
rps = 45                  # requests per second

print("=== Performance Optimization Report ===")

if avg_response_time > 1000:
    print("- Response time is high. Consider optimizing database queries or adding caching.")

if rps > 40:
    print("- High traffic detected. Consider horizontal scaling or load balancing.")

if failure_rate == 0:
    print("- Error rate is healthy (0%).")

print("- Recommendation: Enable autoscaling and monitor response times with Prometheus/Grafana.")