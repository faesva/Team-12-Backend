FROM node:14-alpine AS builder
WORKDIR "/app"
ENV PORT=80
COPY . .
RUN yarn install --frozen-lockfile
RUN yarn build
FROM node:14-alpine AS production
WORKDIR "/app"
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/yarn.lock ./yarn.lock
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/app.development.local ./app.development.local
ENV NODE_ENV=development
RUN yarn install --frozen-lockfile --production
#COPY --from=builder /app/node_modules ./node_modules
EXPOSE 80
CMD [ "sh", "-c", "yarn start:prod"]
