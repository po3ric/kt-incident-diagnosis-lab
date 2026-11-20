from slo import availability, is_slo_met
print(availability(5, 10))  # Should print 0.5
print(availability(5, 0))   # Should print None
print(availability(0, 10))  # Should print 0.0

print(is_slo_met(0.95, 0.9))  # Should print True
print(is_slo_met(0.85, 0.9))  # Should print False
print(is_slo_met(None, 0.9))  # Should print False

