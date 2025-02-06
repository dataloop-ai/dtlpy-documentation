import tutorialsIcon from './assets/site/icons/tutorials.svg';
import onboardingIcon from './assets/site/icons/onboarding.svg';
import resourcesIcon from './assets/site/icons/resources.svg';
import {
  LandingLayout,
  Button,
  Box,
  FlexSection,
  Flex,
  Jumbotron,
  WideTile,
  H1,
  H2,
  NavBar,
} from '@redocly/developer-portal/ui';

interface HomePageProps {
  location: {
    pathname: string;
    search: string;
    hash: string;
  };
}

export default function HomePage({ location }: HomePageProps) {
  return (
    <LandingLayout>
      <Jumbotron>
        <NavBar location={location} standalone={false} />
        <H1>Dataloop Developers Portal</H1>
        <H2>A developer portal for beginners and advanced users</H2>
        <Flex p={20} justifyContent="center">
          <Button variant="outlined" size="xlarge" to="tutorials/getting_started/sdk_overview/chapter.md">
            Get started
          </Button>
        </Flex>
      </Jumbotron>
      <Box my={25}>
        <FlexSection justifyContent="space-around" flexWrap="wrap">
          <WideTile to="tutorials/tutorials.mdx" icon={tutorialsIcon} header="Tutorials">
            Step-by-step guides to get started with Dataloop
          </WideTile>
          <WideTile to="onboarding/onboarding.md" icon={onboardingIcon} header="Onboarding">
            Get up and running with Dataloop platform
          </WideTile>
          <WideTile to="resources/resources.mdx" icon={resourcesIcon} header="Resources">
            SDKs, APIs and developer tools
          </WideTile>
        </FlexSection>
      </Box>
    </LandingLayout>
  );
}

