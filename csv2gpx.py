#!/usr/bin/env python3
import sys
import gpxpy
import csv


def csv2gpx(fnp):

    with open(fnp, newline="") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        line = 0
        reader = csv.reader(csvfile, dialect)
        row = names = next(reader)
        gpx = gpxpy.gpx.GPX()
        # Create first track in our GPX:
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        for row in reader:
            line += 1
            columns = len(row)
            lat = row[0]
            lon = row[1]
            pt = gpxpy.gpx.GPXTrackPoint(float(lat), float(lon))
            d = ""
            for i in range(2, columns):
                d += names[i] + ": " + row[i] + "\n"
            pt.description = d
            gpx_segment.points.append(pt)

    gpx.creator = f"Fida csv file "
    gpx.name = fnp
    return gpx


def main():

    for filename in sys.argv[1:]:
        gpx = csv2gpx(filename)
        print(gpx.to_xml())


if __name__ == "__main__":
    main()
