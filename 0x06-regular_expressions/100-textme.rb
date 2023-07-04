#!/usr/bin/env ruby
# Parsing logfile and output
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
