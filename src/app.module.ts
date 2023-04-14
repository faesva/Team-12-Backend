import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { TypeOrmModule, TypeOrmModuleOptions } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import appConfig, {
  jwtConfig,
} from './config/app.config';
import { DATABASE_CONFIG } from './config/constants.config';
import { AuthModule } from './auth/auth.module';
import databaseConfig from './config/database.config';
import envValidate from './config/env.validate';
import { CommonModule } from './common/common.module';
import { FilmsModule } from './films/films.module';

const ConfigModuleProvider = ConfigModule.forRoot({
  envFilePath: `.env.${process.env.NODE_ENV ?? 'development'}.local`,
  isGlobal: true,
  load: [databaseConfig, appConfig, jwtConfig],
  validationSchema: envValidate,
});

const TypeOrmModuleProvider = TypeOrmModule.forRootAsync({
  inject: [ConfigService],
  useFactory: (configService: ConfigService) =>
    configService.get<TypeOrmModuleOptions>(DATABASE_CONFIG),
});

@Module({
  imports: [
    ConfigModuleProvider,
    TypeOrmModuleProvider,
    AuthModule,
    CommonModule,
    FilmsModule,
  ],
  controllers: [AppController],
})
export class AppModule {}
