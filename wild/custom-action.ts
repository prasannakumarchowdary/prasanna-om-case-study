import { createTemplateAction } from '@backstage/plugin-scaffolder-node';
import fs from 'fs';
import path from 'path';

export const createMyCustomAction = () => {
  return createTemplateAction({
    id: 'my:custom:action',
    schema: {
      input: {
        type: 'object',
        properties: {
          filename: { type: 'string' },
        },
      },
    },
    async handler(ctx) {
      const filePath = path.join(ctx.workspacePath, ctx.input.filename || 'output.txt');
      fs.writeFileSync(filePath, 'Hello from custom action');
    },
  });
};
