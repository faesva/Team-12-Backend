import { Connection, getManager } from 'typeorm';
import { Factory, Seeder } from 'typeorm-seeding';

export class RolSeed implements Seeder {
  public async run(factory: Factory, connection: Connection): Promise<void> {
    await getManager().query('TRUNCATE roles CASCADE');
    await getManager().query(
      'INSERT INTO roles ("id", "createdAt", "updatedAt", "name") VALUES (1, now(), now(), \'USER\'), (2, now(), now(), \'ADMIN\');',
    );
  }
}
