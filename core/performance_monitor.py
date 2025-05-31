import time
import threading
from typing import Dict, Any
from contextlib import contextmanager
from collections import defaultdict

class PerformanceMonitor:
    """Simple performance monitoring."""
    
    def __init__(self):
        self.execution_times = defaultdict(list)
        self.lock = threading.Lock()
        self.start_time = time.time()
    
    @contextmanager
    def track_execution(self, operation_name: str):
        """Context manager to track execution time."""
        start_time = time.time()
        try:
            yield
        finally:
            execution_time = time.time() - start_time
            with self.lock:
                self.execution_times[operation_name].append(execution_time)
                # Keep only last 100 entries
                if len(self.execution_times[operation_name]) > 100:
                    self.execution_times[operation_name] = self.execution_times[operation_name][-100:]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get performance statistics."""
        with self.lock:
            stats = {
                "monitoring_available": True,
                "uptime_seconds": round(time.time() - self.start_time, 2),
                "system": {
                    "active_threads": threading.active_count(),
                    "current_time": time.strftime("%Y-%m-%d %H:%M:%S")
                },
                "execution_times": {}
            }
            
            # Add system stats if psutil is available
            try:
                import psutil
                stats["system"].update({
                    "cpu_percent": psutil.cpu_percent(),
                    "memory_percent": psutil.virtual_memory().percent
                })
            except ImportError:
                stats["system"]["note"] = "Install psutil for system monitoring"
            
            # Process execution times
            for operation, times in self.execution_times.items():
                if times:
                    stats["execution_times"][operation] = {
                        "avg_seconds": round(sum(times) / len(times), 3),
                        "min_seconds": round(min(times), 3),
                        "max_seconds": round(max(times), 3),
                        "count": len(times),
                        "last_execution": round(times[-1], 3)
                    }
            
            return stats
    
    def stop_monitoring(self):
        """Stop monitoring (placeholder for compatibility)."""
        pass