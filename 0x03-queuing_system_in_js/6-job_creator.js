import { createQueue } from 'kue';
const queue = createQueue({name: 'push_notification_code'});

const data = {
  phoneNumber: "0700000000",
  message: "unknown",
};

const job = queue
  .create("push_notification_code", data)
  .save((err) => {
    if (!err) console.log("Notification job created:", job.id);
  })
  .on("complete", () => console.log("Notification job completed"))
  .on("failed", () => console.log("Notification job failed"));
