import csv

class SensorPipeline:

    def __init__(self, threshold, alpha):

        self.threshold = threshold
        self.alpha = alpha

        self.estimate = None

        self.raw_data = []
        self.smooth_data = []

    def parse(self, value):
        return float(value)

    def validate(self, value):

        if value < -50 or value > 150:
            return False

        return True

    def smooth(self, value):

        if self.estimate is None:
            self.estimate = value

        self.estimate = self.estimate + self.alpha * (value - self.estimate)

        return self.estimate

    def log(self, writer, index, raw, smooth):

        writer.writerow([
            index,
            round(raw,2),
            round(smooth,2)
        ])

    def alert(self, value):

        if value > self.threshold:
            print(f"⚠ WARNING : High Temperature ({value:.2f}°C)")

    def run(self, sensor, total):

        with open("sensor_log.csv","w",newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Reading",
                "Raw Temperature",
                "Smoothed Temperature"
            ])

            for i in range(total):

                raw = sensor.read()

                raw = self.parse(raw)

                if self.validate(raw):

                    smooth = self.smooth(raw)

                    self.raw_data.append(raw)
                    self.smooth_data.append(smooth)

                    self.log(writer,i+1,raw,smooth)

                    self.alert(raw)