import { Module } from '@nestjs/common';
import { FilmsService } from './services/films.service';
import { FilmsController } from './controllers/films.controller';

@Module({
  controllers: [FilmsController],
  providers: [FilmsService],
})
export class FilmsModule {}
