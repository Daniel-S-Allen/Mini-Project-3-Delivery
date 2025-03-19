# loglens.py - Main application entry point

import argparse
import sys
from typing import cast
from log_parser import LogParser
from log_analyzer import LogAnalyzer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="LogLens - A log analysis and monitoring tool")
    _ = parser.add_argument("log_file", help="Path to the log file to analyze")
    _ = parser.add_argument("-f", "--format", choices=["txt", "csv"], default="txt", help="Output format (default: txt)")
    _ = parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    _ = parser.add_argument("-d", "--date-range", help="Filter by date range (format: YYYY-MM-DD:YYYY-MM-DD)")
    _ = parser.add_argument("-s", "--severity", choices=["INFO", "WARNING", "ERROR", "CRITICAL"], help="Filter by severity level")
    _ = parser.add_argument("-p", "--pattern", help="Filter by regex pattern")
    _ = parser.add_argument("--stats", action="store_true", help="Generate statistics")
    _ = parser.add_argument("--alerts", help="Generate alerts for error rates above threshold (float value)")
    
    args = parser.parse_args()
    
    try:
        # Initialize components
        parser = LogParser()
        analyzer = LogAnalyzer()
        generator = ReportGenerator()
        
        # Parse logs
        log_entries = parser.parse_file(cast(str,args.log_file))
        
        # Apply filters
        if cast(str,args.date_range):
            start_date, end_date = cast(str,args.date_range).split(":")
            log_entries = analyzer.filter_by_date(log_entries, start_date, end_date)
        
        if cast(str,args.severity):
            log_entries = analyzer.filter_by_severity(log_entries, cast(str,args.severity))
        
        if cast(str,args.pattern):
            log_entries = analyzer.filter_by_pattern(log_entries, cast(str,args.pattern))
        
        # Analyze logs
        if cast(str,args.stats):
            stats = analyzer.generate_statistics(log_entries)
        else:
            stats = None
        
        # Generate alerts if threshold is provided
        alerts = None
        if cast(str,args.alerts):
            threshold = float(cast(str,args.alerts))
            alerts = analyzer.check_alerts(log_entries, threshold)
        
        # Generate report
        report = generator.generate_report(log_entries, format=cast(str,args.format), stats=stats, alerts=alerts)
        
        # Output report
        if cast(str,args.output):
            with open(cast(str,args.output), 'w') as f:
                _ = f.write(report)
        else:
            print(report)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
