const blackList = ["4153518780", "4153518781"];

import { createQueue } from 'kue';
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  for (let i = 0; i <= 100; i++) {
    if (i == 0) {
      job.progress(0, 100);
      if (blackList.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      }
    } else if (i == 50) {
      job.progress(50, 100);
      console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
      );
    }
  }
  done();
}

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
