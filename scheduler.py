"""
Scheduling Module for Random Posting Times
Handles random time scheduling within specified ranges
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List


class PostScheduler:
    def __init__(self, config: dict):
        self.config = config
        self.post_times = config.get('automation', {}).get('post_times', [])
        self.random_range = config.get('automation', {}).get('random_time_range', 30)
    
    def get_next_posting_time(self) -> datetime:
        """
        Get the next scheduled posting time
        Adds random offset based on configuration
        """
        if not self.post_times:
            # Default to 9 AM if no times configured
            next_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
            
            # If already past 9 AM today, schedule for tomorrow
            if datetime.now() >= next_time:
                next_time += timedelta(days=1)
        else:
            # Get next scheduled time
            next_time = self._get_next_scheduled_time()
        
        # Add random offset
        random_minutes = random.randint(-self.random_range, self.random_range)
        next_time += timedelta(minutes=random_minutes)
        
        return next_time
    
    def _get_next_scheduled_time(self) -> datetime:
        """Get the next scheduled time from configured list"""
        now = datetime.now()
        today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        times_today = []
        for time_config in self.post_times:
            hour = time_config['hour']
            minute = time_config['minute']
            scheduled_time = today.replace(hour=hour, minute=minute)
            
            if scheduled_time > now:
                times_today.append(scheduled_time)
        
        if times_today:
            # Return earliest time today
            return min(times_today)
        else:
            # All times passed, get first time tomorrow
            first_time = self.post_times[0]
            tomorrow = today + timedelta(days=1)
            return tomorrow.replace(hour=first_time['hour'], minute=first_time['minute'])
    
    def is_time_to_post(self) -> bool:
        """Check if it's time to post based on current time"""
        now = datetime.now()
        target_times = self.get_daily_target_times()
        
        for target_time in target_times:
            # Check if within 5 minutes of target time
            time_diff = abs((now - target_time).total_seconds() / 60)
            if time_diff <= 5:
                return True
        
        return False
    
    def get_daily_target_times(self) -> List[datetime]:
        """Get all target posting times for today with random offsets"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        target_times = []
        for time_config in self.post_times:
            hour = time_config['hour']
            minute = time_config['minute']
            base_time = today.replace(hour=hour, minute=minute)
            
            # Add random offset
            random_minutes = random.randint(-self.random_range, self.random_range)
            target_time = base_time + timedelta(minutes=random_minutes)
            
            # Only include future times
            if target_time > datetime.now():
                target_times.append(target_time)
        
        return sorted(target_times)
    
    def get_schedule_summary(self) -> str:
        """Get human-readable schedule summary"""
        summary = "📅 Posting Schedule:\n"
        
        targets = self.get_daily_target_times()
        if targets:
            for i, target in enumerate(targets, 1):
                summary += f"   {i}. {target.strftime('%I:%M %p')} (±{self.random_range} min)\n"
        else:
            summary += "   No scheduled posts for today\n"
        
        return summary


def get_next_posting_time(config: dict) -> datetime:
    """Get next posting time"""
    scheduler = PostScheduler(config)
    return scheduler.get_next_posting_time()

def is_time_to_post(config: dict) -> bool:
    """Check if it's time to post"""
    scheduler = PostScheduler(config)
    return scheduler.is_time_to_post()


if __name__ == "__main__":
    # Test scheduler
    config = {
        'automation': {
            'post_times': [
                {'hour': 9, 'minute': 30},
                {'hour': 14, 'minute': 15},
                {'hour': 18, 'minute': 45}
            ],
            'random_time_range': 30
        }
    }
    
    scheduler = PostScheduler(config)
    print(scheduler.get_schedule_summary())
    
    next_time = scheduler.get_next_posting_time()
    print(f"\nNext posting time: {next_time.strftime('%Y-%m-%d %I:%M %p')}")

