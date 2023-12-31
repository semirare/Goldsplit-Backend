import xml.etree.ElementTree as ET

from rest_framework.exceptions import ParseError
from datetime import datetime
from statistics import mean

from .timeUtils import timeToMs

def parseSplits(file):
    #parses uploaded splits file
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        formattedSplits = []
        total_time = gold_total_time = average_total_time = previous_segment_time = 0

        for elem in root.iter('Segments'):
            segments = elem.findall('Segment')
            for split in segments:

                #we don't currently support subsplits which can make names look weird
                #to fix this we have to:
                #1) remove any leading '-' which denotes a subsplit
                #2) remove any leading text enclosed in a set of brackets { } which denotes a subsplit section header
                name = split.find('Name').text
                if name[0] == '-':
                    name = name[1:]
                elif name[0] == '{':
                    #split the string into 2 pieces at the first closing brace and take the second piece of the string as the name
                    name = name.split('}',1)[-1]

                #livesplit gives us the total time for the split so we need to track the previous segment time and remove it
                #in order to just get the segment time
                time = timeToMs(split.find('SplitTimes/SplitTime/RealTime').text) - previous_segment_time
                total_time += time

                #update previous segment time for next loop
                previous_segment_time = total_time

                gold_time = timeToMs(split.find('BestSegmentTime/RealTime').text)
                gold_total_time += gold_time

                #keep track of all segment times to get average
                seg_times = []
                for seg in split.findall('SegmentHistory/Time/RealTime'):
                    seg_times.append(timeToMs(seg.text))

                average_time = round(mean(seg_times))
                average_total_time += average_time

                formattedSplits.append(
                    {
                        'name': name,
                        'time': time,
                        'total_time': total_time,
                        'gold_time': gold_time,
                        'gold_total_time': gold_total_time,
                        'average_time': average_time,
                        'average_total_time': average_total_time
                    }
                )
            
        splits_info = {
            'game_name': root.find('./GameName').text,
            'category': root.find('./CategoryName').text,
            'time': total_time,
            'splits': formattedSplits
        }

        return splits_info
                
    except:
        raise ParseError()