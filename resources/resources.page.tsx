import React from 'react';
import styled from 'styled-components';
import { Card } from '@redocly/theme/markdoc/components/Cards/Card';
import { Cards } from '@redocly/theme/markdoc/components/Cards/Cards';

import pythonSdkIcon from '../assets/site/icons/python-sdk.svg';
import jsSdkIcon from '../assets/site/icons/js-sdk.svg';

const Container = styled.div`
  padding: 2rem;
`;

const ResourcesPage = () => (
  <Container>
    <Cards>
      <Card title="Python SDK" to="https://sdk-docs.dataloop.ai/en/latest/_modules/index.html" icon={pythonSdkIcon}>
        Complete Python SDK documentation and API reference
      </Card>
      <Card title="JavaScript SDK" to="dtljs/index.md" icon={jsSdkIcon}>
        Complete JavaScript SDK documentation and API reference
      </Card>
      <Card title="REST API" to="https://docs.dataloop.ai/reference/rest-api" icon={jsSdkIcon}>
        Complete REST API documentation and API reference
      </Card>
    </Cards>
  </Container>
);

export default ResourcesPage;
