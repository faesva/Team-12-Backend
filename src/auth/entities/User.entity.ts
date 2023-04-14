import {
  BeforeInsert,
  BeforeUpdate,
  Column,
  Entity,
  JoinColumn,
  ManyToOne,
} from 'typeorm';
import { hash } from 'bcryptjs';
import { Rol } from '@app/auth/entities/Rol.entity';
import { AbstractEntity } from '@app/common/entities/AbstractEntity.entity';

@Entity('users')
export class User extends AbstractEntity {
  @Column()
  completeName: string;

  @Column({ unique: true })
  email: string;

  @Column()
  phone: string;

  @Column({ type: 'varchar', select: false })
  password: string;

  @Column({ type: 'boolean', default: true })
  status: boolean;

  @BeforeInsert()
  @BeforeUpdate()
  async hashPassword() {
    if (!this.password) return;
    this.password = await hash(this.password, 10);
  }

  @JoinColumn()
  @ManyToOne((_) => Rol, (rol) => rol.users, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  rol: Rol;
}
