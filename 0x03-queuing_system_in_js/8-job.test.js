import { expect } from 'chai';
import mocha from 'mocha';
import kue from 'kue';
import { createPushNotificationsJobs } from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });

  it('error thrown when jobs is not an array', (done) => {
    expect(() => createPushNotificationsJobs('string', queue))
      .to.throw(Error, 'Jobs is not an array');
    done();
  });

  it('3 jobs created successfully', () => {
    const jobs = [
      {name: 'job 1'},
      {name: 'job 2'},
      {name: 'job 3'}
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(3);
    expect(queue.testMode.jobs[0].type).to.be.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.name).to.be.equal('job 1');
    expect(queue.testMode.jobs[1].type).to.be.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data.name).to.be.equal('job 2');
  });

  // it()
});
